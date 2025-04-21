# structured-logging-python-package
python library for structure logging

### How to install and use the Python Structured Logging logger
1. Install it using PIP: pip install git+https://github.com/Givelify/structured-logging-python-package.git
2. Or add this line to requirements.txt file: givelifylogging @ git+https://github.com/Givelify/structured-logging-python-package.git
3. To create the logger in your Python code:
4.   from givelifylogging import StructuredLogger as slogger
5.   
6.   logger = slogger.StructuredLogger.getLogger(<module name>, <Log Level String: Optional>, <Log handler : Optional>, <Log location: Optional>, <Log File Name: Optional>)
