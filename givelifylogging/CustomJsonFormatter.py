from pythonjsonlogger import jsonlogger

class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super().add_fields(log_record, record, message_dict)
        # This will ensure the 'message' attribute is populated
        log_record['message'] = record.getMessage()
        # Populate other attributes, if they are missing
        log_record['level'] = log_record.get('level', record.levelno)
        log_record['level_name'] = log_record.get('levelname', record.levelname)
        log_record['datetime'] = log_record.get('asctime', self.formatTime(record))
        # Extract context entity from `extra`, defaulting to provided values if not present
        context = log_record.pop('context', {})
        log_record.update({
            "context": {
                "givelifyEventId": context.get('givelifyEventId', None),
                "entity": context.get('entity', {})
            }
        })