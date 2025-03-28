import logging

class StructuredLogger:
    def __init__(self, base_logger):
        self.logger = base_logger
        
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
