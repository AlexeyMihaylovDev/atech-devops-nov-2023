import time
from pathlib import Path
from detect import run
import yaml
from loguru import logger
import os
import boto3

bucket_name = os.environ['BUCKET_NAME']
queue_name = os.environ['SQS_QUEUE_NAME']

sqs_client = boto3.client('sqs', region_name='ap-northeast-2')

with open("data/coco128.yaml", "r") as stream:
    names = yaml.safe_load(stream)['names']


def consume():
    while True:
        response = sqs_client.receive_message(QueueUrl=queue_name, MaxNumberOfMessages=1, WaitTimeSeconds=5)

        if 'Messages' in response:
            message = response['Messages'][0]['Body']
            receipt_handle = response['Messages'][0]['ReceiptHandle']

            # Use the ReceiptHandle as a prediction UUID
            prediction_id = response['Messages'][0]['MessageId']

            logger.info(f'prediction: {prediction_id}. start processing')

            # Receives a URL parameter representing the image to download from S3
            message = json.loads(message)
            img_name = message['image'] # TODO extract from `message`
            chat_id = message['chat_id'] # TODO extract from `message`
            # TODO download img_name from S3, store the local image path in original_img_path
            s3 = boto3.client('s3')
            original_img_path = str(img_name)
            try:
                s3.download_file(images_bucket, img_name, original_img_path)
                logger.info(f'Downloading image completed')

            except NoCredentialsError:
                logger.error("AWS credentials not available.")
                return None
            except Exception as e:
                logger.error(f"uploading photo to S3 Failed: {e}")
                return None

            # Predicts the objects in the image
            run(
                weights='yolov5s.pt',
                data='data/coco128.yaml',
                source=original_img_path,
                project='static/data',
                name=prediction_id,
                save_txt=True
            )

            logger.info(f'prediction: {prediction_id}/{original_img_path}. done')

            # This is the path for the predicted image with labels
            # The predicted image typically includes bounding boxes drawn around the detected objects, along with class labels and possibly confidence scores.
            predicted_img_path = Path(f'static/data/{prediction_id}/{original_img_path}')

            # TODO Uploads the predicted image (predicted_img_path) to S3 (be careful not to override the original image).
            the_image = original_img_path[:-4] + "_predicted.jpg"
            s3.upload_file(predicted_img_path, bucket_name, the_image)
            # Parse prediction labels and create a summary
            pred_summary_path = Path(f'static/data/{prediction_id}/labels/{original_img_path.split(".")[0]}.txt')
            if pred_summary_path.exists():
                with open(pred_summary_path) as f:
                    labels = f.read().splitlines()
                    labels = [line.split(' ') for line in labels]
                    labels = [{
                        'class': names[int(l[0])],
                        'cx': float(l[1]),
                        'cy': float(l[2]),
                        'width': float(l[3]),
                        'height': float(l[4]),
                    } for l in labels]

                logger.info(f'prediction: {prediction_id}/{original_img_path}. prediction summary:\n\n{labels}')

                prediction_summary = {
                    'prediction_id': prediction_id,
                    'original_img_path': original_img_path,
                    'predicted_img_path': predicted_img_path,
                    'labels': labels,
                    'time': time.time()
                }

                # TODO store the prediction_summary in a DynamoDB table
                try:
                    obj = [item['class'] for item in labels]
                    obj_count = Counter(obj)
                    obj_str = ', '.join(obj)
                    obj_count_str = ', '.join(f'{key}: {value}' for key, value in obj_count.items())
                    logger.info(
                        f'objects: {obj}\n\n objects_count: {obj_count}\n\n objects_count_str: {obj_count_str}\n\n')
                    logger.info(
                        f'prediction_id: {prediction_id}\n original_img_path {original_img_path}\n. predicted_img_path {predicted_img_path}\n chat_id {chat_id}\n labels :{labels}\n\n objects: {obj}\n\n')

                    logger.info(f'type of lables :{type(labels)}')
                    dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')
                    table = dynamodb.Table('ahmadbaloum-db')
                    table.put_item(
                        Item={
                            'prediction_id': prediction_id,
                            'original_img_path': original_img_path,
                            'chat_id': chat_id,
                            'labels': obj_str
                        }
                    )
                    logger.info(
                        f'\n Added Data to dynamodb : {dynamodb}. data :\n\n{prediction_id}\n\n{original_img_path}\n\n{predicted_img_path}\n\n{chat_id}')
                    logger.info(
                        f'\n prediction: {prediction_id}/{original_img_path}. prediction summary lables :\n\n{obj_str}')

                    # sqs_client.delete_message(QueueUrl=queue_name, ReceiptHandle=receipt_handle)
                    logger.info(f'sqs delete queue name : {queue_name}/{receipt_handle}. message deleted from queue')
                except Exception as e:
                    logger.error(f'Error updating dynamo: {e}')

                # TODO perform a GET request to Polybot to `/results` endpoint
                url = f'https://ahmad-baloum-1107395860.ap-northeast-2.elb.amazonaws.com/results/?predictionId={prediction_id}'
                logger.info(f'url: {url}')
                response = requests.get(url, verify=False)
                logger.info(f'response: {response}')
            # Delete the message from the queue as the job is considered as DONE
            sqs_client.delete_message(QueueUrl=queue_name, ReceiptHandle=receipt_handle)


if __name__ == "__main__":
    consume()
