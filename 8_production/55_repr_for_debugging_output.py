
print('foo bar')
print('%s' % 'foo bar')
print(5)
print('5')
# >>>
# foo bar
# foo bar
# 5
# 5
## human readable, but type?


a = '\x07'
print(repr(a))
b = eval(repr(a))
assert a == b
# >>> 
# '\x07'


print(repr(5))
print(repr('5'))
print('%r' % 5)
print('%r' % '5')
# >>>
# 5
# '5'
# 5
# '5'


class OpaqueClass(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = OpaqueClass(1, 2)
print(obj)
# >>>
# <__main__.OpaqueClass object at 0x1016b9cf8>


class BetterClass(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return 'BetterClass(%d, %d)' % (self.x, self.y)

obj = BetterClass(1, 2)
print(obj)
# >>>
# BetterClass(1, 2)


obj = OpaqueClass(4, 5)
print(obj.__dict__)
# >>>
# {'y': 5, 'x': 4}
