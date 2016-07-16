
def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('%s(%r, %r) -> %r' %
            (func.__name__, args, kwargs, result))
        return result
    return wrapper

@trace # fibonacci = trace(fibonacci)
def fibonacci(n):
    if n in (0, 1):
        return n
    return (fibonacci(n-2) + fibonacci(n-1))

fibonacci(3)
# >>>
# fibonacci((1,), {}) -> 1
# fibonacci((0,), {}) -> 0
# fibonacci((1,), {}) -> 1
# fibonacci((2,), {}) -> 1
# fibonacci((3,), {}) -> 2

# f(3) 5 = f(1) 1 + f(2) 4
# f(2) 4 = f(0) 2 + f(1) 3

print(fibonacci)
# >>>
# <function trace.<locals>.wrapper at 0x10114c268>

help(fibonacci)
# >>>
# Help on function wrapper in module __main__:

# wrapper(*args, **kwargs)


from functools import wraps
def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('%s(%r, %r) -> %r' %
            (func.__name__, args, kwargs, result))
        return result
    return wrapper

@trace
def fibonacci(n):
    if n in (0, 1):
        return n
    return (fibonacci(n-2) + fibonacci(n-1))

print(fibonacci)
# >>>
# <function fibonacci at 0x10114c2f0>

help(fibonacci)
# >>>
# Help on function fibonacci in module __main__:

# fibonacci(n)