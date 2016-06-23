
import datetime, time
def log(message, when=datetime.datetime.now()):
    print('%s: %s' % (when, message))

log('Hi there')
time.sleep(0.1)
log('Hi again')
# >>>
# 2016-06-23 20:16:17.325088: Hi there
# 2016-06-23 20:16:17.325088: Hi again


def log2(message, when=None):
    """ Log a message with a timestamp.
    
    Args:
        message: Message to print.
        when: datetime of when the message occurred.
            Defaults to the present time.
    """
    when = datetime.datetime.now() if when is None else when
    print('%s: %s' % (when, message))

log2('Hi there')
time.sleep(0.1)
log2('Hi again')
# >>>
# 2016-06-23 20:16:17.428694: Hi there
# 2016-06-23 20:16:17.533160: Hi again


import json
def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)
# >>>
# Foo: {'stuff': 5, 'meep': 1}
# Bar: {'stuff': 5, 'meep': 1}

assert foo is bar


def decode2(data, default=None):
    """Load JSON data from a string.

    Args:
        data: JSON data to decode.
        default: Value to return if decoding fails.
            Defaults to an empty dictionary.
    """
    if default is None:
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decode2('bad data')
foo['stuff'] = 5
bar = decode2('also bad')
bar['meep'] = 1
print('Foo:', foo)
print('Bar:', bar)
# >>>
# Foo: {'stuff': 5}
# Bar: {'meep': 1}