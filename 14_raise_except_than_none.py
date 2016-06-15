
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

x, y = 0, 1
result = divide(x, y)
if result is None:
    print('Invalid Inputs')
# >>>
# Invalid Inputs

if not result: # None(0 or '') as False in condition
    print('Invalid Inputs (wrong)')
# >>>
# Invalid Inputs


def divide2(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None

success, result = divide2(x, y)
if not success:
    print('Invalid Inputs')
# >>>
# Invalid Inputs

_, result = divide2(x, y)
if not result:
    print('Invalid Inputs')
# >>>
# Invalid Inputs


def divide3(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e

x, y = 5, 2
try:
    result = divide3(x, y)
except ValueError:
    print('Invalid Inputs')
else:
    print('Result is %.1f' % result)


