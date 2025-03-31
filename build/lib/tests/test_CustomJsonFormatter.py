import logging
import pytest
import re
import json
from io import StringIO

from givelifylogging import CustomJsonFormatter

def log_message(buffer, msg, context):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(buffer)
    formatter = CustomJsonFormatter.CustomJsonFormatter('{"message": "%(message)s", "level": "%(levelname)s", "name": "%(name)s", "asctime": "%(asctime)s"}', datefmt='%Y-%m-%d %H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info(msg, extra=context)

def test_log_format(caplog):
    # Configure caplog to capture log messages
    caplog.set_level(logging.INFO)

    # Call the function that logs a message
    msg = "Something happened"
    buffer = StringIO()
    log_message(buffer, msg, {"context": {"givelifyEventId": 123, "entity": {}}})

    # Assert that a log message was emitted
    assert len(caplog.records) == 1

    # print("***************** Output : " + buffer.getvalue())

    # Assert the log format as a json object
    log_record = json.loads(buffer.getvalue())

    assert log_record['level'] == logging.INFO
    assert log_record['message'] == msg
    assert log_record['context']['givelifyEventId'] == 123
    assert log_record['context']['entity'] == {}