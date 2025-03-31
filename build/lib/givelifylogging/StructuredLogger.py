import logging
import datetime
import os
from logging.handlers import TimedRotatingFileHandler
from givelifylogging.CustomJsonFormatter import CustomJsonFormatter

class StructuredLogger:
    def __init__(self, base_logger):
        self.logger = base_logger
        formatted_log_filename = f"logFile-{datetime.datetime.now().strftime('%Y-%m-%d')}.log"
        self.filepath = os.path.join('.logs', formatted_log_filename)

    def setLogFile(self, filepath):
        self.filepath = filepath
    
    def getLogFile(self):
        return self.filepath
    
    def log(self, message, type_="generic", value=None, level=logging.INFO):
        if value is None:
            value = {}
        context_data = {
            "givelifyEventId": None,
            "entity": {
                "type": type_,
                "value": value
            }
        }
        self.logger.log(level, message, extra={"context": context_data})

    def info(self, message, type_="generic", value=None):
        self.log(message, type_, value, logging.INFO)

    def warn(self, message, type_="generic", value=None):
        self.log(message, type_, value, logging.WARNING)

    def error(self, message, type_="generic", value=None):
        self.log(message, type_, value, logging.ERROR)

    def debug(self, message, type_="generic", value=None):
        self.log(message, type_, value, logging.DEBUG)

    def critical(self, message, type_="generic", value=None):
        self.log(message, type_, value, logging.CRITICAL)

    def getLogger(__name__, handler=None, folder='.logs', filename='logFile'):
        if not os.path.exists(folder):
            os.makedirs(folder)

        formatted_log_filename = f"{filename}-{datetime.datetime.now().strftime('%Y-%m-%d')}.log"
        log_file = os.path.join(folder, formatted_log_filename)

        base_logger = logging.getLogger(__name__)
        base_logger.setLevel(logging.INFO)

        if not handler:
            handler = TimedRotatingFileHandler(log_file, when="midnight", interval=1, backupCount=3, encoding='utf-8')
            handler.suffix = "%Y-%m-%d.log"

        # formatter = CustomJsonFormatter('(message) (levelname) (name) (asctime)', datefmt='%Y-%m-%d %H:%M:%S')
        formatter = CustomJsonFormatter('{"message": "%(message)s", "level": "%(levelname)s", "name": "%(name)s", "asctime": "%(asctime)s"}', datefmt='%Y-%m-%d %H:%M:%S')

        handler.setFormatter(formatter)
        base_logger.addHandler(handler)

        logger = StructuredLogger(base_logger)
        logger.setLogFile(log_file)
        
        return logger
    

