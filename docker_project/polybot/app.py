import flask
from flask import request
import os
from bot import ObjectDetectionBot, Bot

app = flask.Flask(__name__)

#TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
#TELEGRAM_APP_URL = os.environ['TELEGRAM_APP_URL']

TELEGRAM_TOKEN='6810278453:AAHAp9L-0y4t0WupwoL_hBzaZQDzISSCYkI'
TELEGRAM_APP_URL='t.me/MSHSHAGAL_BOT'

@app.route('/', methods=['GET'])
def index():
    return 'Ok'


@app.route(f'/{TELEGRAM_TOKEN}/', methods=['POST'])
def webhook():
    req = request.get_json()
    bot.handle_message(req['message'])
    return 'Ok'


if __name__ == "__main__":
    bot = Bot(TELEGRAM_TOKEN, TELEGRAM_APP_URL)

    app.run(host='0.0.0.0', port=8443)
