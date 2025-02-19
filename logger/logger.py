import logging
import json

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            'timestamp': record.created,
            'message': record.getMessage(),
            'level': record.levelno,
        }
        return json.dumps(log_record)
def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setFormatter(JsonFormatter())
    logger.addHandler(handler)
    return logger