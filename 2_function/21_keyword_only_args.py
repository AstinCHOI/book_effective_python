
def safe_division(number, divisor, ignore_overflow, 
                  ignore_zero_division):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

result = safe_division(1, 10**500, True, False)
print(result)
result = safe_division(1, 0, False, True)
print(result)
# >>>
# 0.0
# inf

def safe_division2(number, divisor, 
                  ignore_overflow=False, 
                  ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

result = safe_division2(1, 10**500, ignore_overflow=True)
print(result)
result = safe_division2(1, 0, ignore_zero_division=True)
print(result)
# >>>
# 0.0
# inf
# result = safe_division2(1, 10**500, True, False) # okay


import sys
if sys.version_info[0] >= 3:
    def safe_division3(number, divisor, *, 
                    ignore_overflow=False, 
                    ignore_zero_division=False):
        try:
            return number / divisor
        except OverflowError:
            if ignore_overflow:
                return 0
            else:
                raise
        except ZeroDivisionError:
            if ignore_zero_division:
                return float('inf')
            else:
                raise

    # result = safe_division3(1, 10**500, True, False) # not okay
    # >>> 
    # TypeError: safe_division3() takes 2 positional arguments but 4 were given
    result = safe_division3(1, 0, ignore_zero_division=True) # okay
    print(result)
    # >>>
    # inf

    try:
        safe_division3(1, 0)
    except ZeroDivisionError:
        pass # run as expected


# for python2
def print_args(*args, **kwargs):
    print('Positional:', args)
    print('Keyword:   ', kwargs)

print_args(1, 2, foo='bar', stuff='meep')
# >>>
# Positional: (1, 2)
# Keyword:    {'stuff': 'meep', 'foo': 'bar'}


def safe_division4(number, divisor, **kwargs):
    ignore_overflow = kwargs.pop('ignore_overflow', False)
    ignore_zero_div = kwargs.pop('ignore_zero_division', False)
    if kwargs:
        raise TypeError('Unexpected **kwargs: %r' % kwargs)

safe_division4(1, 10)
safe_division4(1, 0, ignore_zero_division=True)
safe_division4(1, 10**500, ignore_overflow=True)

# safe_division4(1, 10**500, True, False) # not okay
# >>> 
# TypeError: safe_division4() takes 2 positional arguments but 4 were given

# safe_division4(0, 0, unexpected=True) # not okay
# >>>
# TypeError: Unexpected **kwargs: {'unexpected': True}