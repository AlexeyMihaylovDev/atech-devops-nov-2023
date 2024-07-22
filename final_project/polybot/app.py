import json
import os
import flask
import boto3
import telebot
from bot import ObjectDetectionBot
import time
import requests
from flask import request
from loguru import logger
from botocore.exceptions import ClientError
from telebot.types import InputFile
from collections import Counter


app = flask.Flask(__name__)

TELEGRAM_APP_URL = os.environ['WEBHOOK_URL']
region_name= os.environ['AWS_REGION']

def get_secret():
    secret_name = "telegram-polybot-token"
    region_name = "ap-northeast-2"

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        error_message = f"Failed to retrieve secret '{secret_name}' from Secrets Manager: {e}"
        raise ValueError(error_message) from None

    if 'SecretString' in response:
        secret_string = response['SecretString']
    else:
        raise ValueError("Secret value not found")

    try:
        secret_value = json.loads(secret_string)['TELEGRAM_TOKEN']
    except json.JSONDecodeError:
        raise ValueError("Failed to parse secret value as JSON.") from None

    return secret_value


TELEGRAM_TOKEN = get_secret()

logger.info(f"TELEGRAM_APP_URL: {TELEGRAM_APP_URL}")

@app.route('/', methods=['GET'])
def index():
    return 'Ok'


@app.route(f'/{TELEGRAM_TOKEN}/', methods=['POST'])
def webhook():
    req = request.get_json()
    bot.handle_message(req['message'])
    return 'Ok'


@app.route(f'/results/', methods=['GET'])
def results():
    prediction_id = request.args.get('predictionId')

    dynamodb_resource = boto3.resource('dynamodb', region_name=region_name)
    table_name = 'prediction_summary'
    table = dynamodb_resource.Table(table_name)

    try:
        response = table.get_item(
            Key={
                'prediction_id': prediction_id
            }
        )

        if 'Item' in response:
            item = response['Item']
            logger.info("Item retrieved successfully:")
            logger.info(item)
        else:
            logger.info("Item not found.")
    except Exception as e:
        logger.error("Error retrieving item:", exc_info=True)

    labels = item.get('labels', [])
    chat_id = item.get('chat_id', [])

    predicted_img_path = item.get('original_img_path', [])
    logger.info(f"file : {predicted_img_path}")
    download_path = '/usr/src/app/'
    bucket_name = os.environ['BUCKET_NAME']
    file_name = os.path.basename(predicted_img_path)
    logger.info(f"file_name: {file_name}")
    file_path = os.path.join(download_path, file_name)
    logger.info(f"file_path: {file_path}")
    s3 = boto3.client('s3')
    s3.download_file(bucket_name, file_name, file_path)
    print(f"File: {file_path} downloaded to S3")

    class_names = [label.get('class') for label in labels]
    result = "\n".join([f"{class_name} : {count}" for class_name, count in Counter(class_names).items()])
    try:
        bot.send_photo_rep(chat_id, file_path)
    finally:
            os.remove(file_path)

    text_results = "Detected objects:\n" + result
    bot.send_text(chat_id, text_results)
    return 'Ok'

@app.route(f'/loadTest/', methods=['POST'])
def load_test():
    req = request.get_json()
    bot.handle_message(req['message'])
    return 'Ok'


if __name__ == "__main__":
    bot = ObjectDetectionBot(TELEGRAM_TOKEN, TELEGRAM_APP_URL)

    app.run(host='0.0.0.0', port=8443)