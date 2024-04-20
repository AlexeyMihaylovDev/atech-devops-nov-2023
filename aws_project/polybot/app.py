import flask
from flask import request
import os
from bot import ObjectDetectionBot

app = flask.Flask(__name__)


# TODO load TELEGRAM_TOKEN value from Secret Manager
TELEGRAM_TOKEN = '6521616754:AAGPxWVhiBfOKZSwWJ4THvVreggYD5S9Keg'

TELEGRAM_APP_URL = 'https://Daniel-LB-1354148717.eu-west-1.elb.amazonaws.com'


@app.route('/', methods=['GET'])
def index():
    return 'Ok normal'


@app.route(f'/{TELEGRAM_TOKEN}/', methods=['POST'])
def webhook():
    req = request.get_json()
    bot.handle_message(req['message'])
    return 'Ok'


@app.route(f'/results/', methods=['GET'])
def results():
    prediction_id = request.args.get('predictionId')

    # TODO use the prediction_id to retrieve results from DynamoDB and send to the end-user

    chat_id = ...
    text_results = ...

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
