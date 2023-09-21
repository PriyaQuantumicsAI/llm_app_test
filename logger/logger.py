# Author: Priyadharshini Devarajan

# Date: April 28, 2023
# Description: Logger page of the application.

import logging
from logging.handlers import TimedRotatingFileHandler

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # create a formatter that specifies the log message's format
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')

    # create a StreamHandler that sends log messages to standard output
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    # set up a TimedRotatingFileHandler that rotates every day
    file_handler = TimedRotatingFileHandler('logs/app.log', when='midnight', interval=1, backupCount=60)
    file_handler.suffix = '%Y%m%d'
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger
