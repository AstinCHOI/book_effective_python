
from threading import Lock
lock = Lock()
with lock:
    print('Lock is held')
# >>>
# Lock is held

lock.acquire()
try:
    print('Lock is held')
finally:
    lock.release()
# >>>
# Lock is held


import logging
logging.getLogger().setLevel(logging.WARNING) # default
def my_function():
    logging.debug('Some debug data')
    logging.error('Error log here')
    logging.debug('More debug data')

my_function()
# >>>
# ERROR:root:Error log here


from contextlib import contextmanager
@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)

with debug_logging(logging.DEBUG):
    print('Inside:')
    my_function()
print('After:')
my_function()
# >>>
# Inside:
# DEBUG:root:Some debug data
# ERROR:root:Error log here
# DEBUG:root:More debug data
# After:
# ERROR:root:Error log here


# with open('/tmp/my_output.txt', 'w') as handle:
#     handle.write('This is some data!')

@contextmanager
def debug_logging(level, name):
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)

with debug_logging(logging.DEBUG, 'my-log') as logger:
    logger.debug('This is my message!')
    logging.debug('This will not print')
# >>>
# DEBUG:my-log:This is my message!

logger = logging.getLogger('my-log')
logger.debug('Debug will not print')
logger.error('Error will print')
# >>>
# ERROR:my-log:Error will print