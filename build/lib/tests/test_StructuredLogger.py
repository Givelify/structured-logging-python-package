import logging
import pytest
import re
import json
from io import StringIO
import os

from givelifylogging import StructuredLogger

def test_default_format(caplog):
    # Configure caplog to capture log messages
    caplog.set_level(logging.INFO)

    # Create logger with default format
    msg = "Something happened"
    val = 123

    buffer = StringIO()
    handler = logging.StreamHandler(buffer)

    logger = StructuredLogger.StructuredLogger.getLogger("TEST", handler)

    logger.info(msg, value=val)

    # Assert that a log message was emitted
    assert len(caplog.records) == 1

    # print("***************** Output : " + buffer.getvalue())

    # Assert the log format as a json object
    log_record = json.loads(buffer.getvalue())

    assert log_record['level'] == logging.INFO
    assert log_record['message'] == msg
    assert log_record['context']['entity']['value'] == val

def test_default_location(caplog):
    # Configure caplog to capture log messages
    caplog.set_level(logging.INFO)

    # Create logger with default format
    msg = "Something happened"
    val = 123

    buffer = StringIO()

    logger = StructuredLogger.StructuredLogger.getLogger("TEST")

    logger.info(msg, value=val)

    # Assert that a log message was emitted
    assert len(caplog.records) == 1

    filename = logger.getLogFile()

    assert os.path.exists(filename)