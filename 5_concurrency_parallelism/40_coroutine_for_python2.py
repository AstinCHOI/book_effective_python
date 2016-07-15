
def delegated():
    yield 1
    yield 2

def composed():
    yield 'A'
    for value in delegated(): # yield from for python 3
        yield value
    yield 'B'

print(list(composed()))
# >>>
# ['A', 1, 2, 'B']


class MyReturn(Exception):
    def __init__(self, value):
        self.value = value
    
def delegated():
    yield 1
    raise MyReturn(2) # return 2 for python 3
    yield 'Not reached'

def composed():
    try:
        for value in delegated():
            yield value
    except MyReturn as e:
        output = e.value
    
    yield output * 4

print(list(composed()))
# >>>
# [1, 8]