import os

log_file = os.environ.get('pylogger_file', os.path.expanduser('~/pylogger.log'))
log_clean = os.environ.get('pylogger_clean', None)
cancel_key = ord(os.environ.get('pylogger_cancel', '`')[0])
