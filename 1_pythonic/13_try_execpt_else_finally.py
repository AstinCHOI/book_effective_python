
# handle = open('/temp/random_data.txt') # May raise IOError
# try:
#     data = handle.read() # May raise UnicodeDecodeError
# finally:
#     handle.close()

import json
def load_json_key(data, key):
    try:
        result_dict = json.loads(data) # May raise ValueError
    except ValueError as e:
        raise KeyError from e
    else:
        return result_dict[key] # May raise KeyError


print(load_json_key('{"hello":"world"}', 'hello'))


UNDIFINED = object()
def divide_json(path):
    handle = open(path, 'r+') # May raise IOError
    try:
        data = handle.read() # UnicodeDecodeError
        op = json.loads(data) # ValueError
        value = (
            op['numerator'] /
            op['denominator']) # ZeroDivisionError
    except ZeroDivisionError as e:
        return UNDIFINED
    else:
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result) # IOError
        return value
    finally: 
        handle.close() # Always runs
