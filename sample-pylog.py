import os
import logging
import pylogger2azblob

from logging.config import dictConfig
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

LOGGING_ACCOUNT_NAME = os.getenv('LOGGING_ACCOUNT_NAME', '<your-storage-account>')
LOGGING_CONTAINER = os.getenv('LOGGING_CONTAINER', '<your-container-name>')
LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'DEBUG')
LOGGING_FORMATTER = os.getenv('LOGGING_FORMATTER', 'verbose')
LOGGING_FILENAME = os.getenv('LOGGING_FILENAME', '<file-name-you-wanna-output>')
LOGGING_WHEN = os.getenv('LOGGING_WHEN', 'S')
LOGGING_INTERVAL = int(os.getenv('LOGGING_INTERVAL', 60))

LOGGING = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(message)s',
        },
        'verbose': {
            'format': '%(levelname)s %(hostname)s %(currenttime)s %(message)s',
        }
    },
    'handlers': {
        'blob': {
            'class': 'pylogger2azblob.handlers.BlobStorageTimedRotatingFileHandler',
            'account_name': LOGGING_ACCOUNT_NAME,
            'container': LOGGING_CONTAINER,
            'level': LOGGING_LEVEL,
            'formatter': LOGGING_FORMATTER,
            'filename': LOGGING_FILENAME,
            'when': LOGGING_WHEN,
            'interval': LOGGING_INTERVAL
        }
    },
    'loggers': {
        'example': {
            'handlers': ['blob'],
            'level': LOGGING_LEVEL,
        },
    }
}

dictConfig(LOGGING)
logger = logging.getLogger('example')
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')