# Author: Priyadharshini Devarajan
# Date: September 21, 2023
# Description: Flask Application main page to receive/respond API calls.

from flask import Flask, jsonify, request
from controller.controller import AppController
from config import config
from logger.logger import get_logger

app = Flask(__name__)
logger = get_logger(__name__)

@app.route('/')
def index():
    return 'Welcome to my Flask API!'

@app.route('/jarvis_gen_ai_process_text', methods=['POST'])
def process_text():
    app_controller = AppController(logger, config)
    result = app_controller.jarvis_gen_ai_process_text(request.json)
    return jsonify(result)

if __name__ == '__main__':
    logger.info('Starting APP')
    app.run()
    #app.run(host='0.0.0.0', port=5000)
