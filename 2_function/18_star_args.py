
def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))
    
log('My numbers are', [1, 2])
log('Hi there', [])


def log2(message, *values): #
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s' % (message, values_str))

log2('My numbers are', [1, 2])
log2('Hi there') #
# >>>
# My numbers are: 1, 2
# Hi there

favorites = [7, 33, 99]
log2('Favorite colors', favorites)
log2('Favorite colors', *favorites)
# >>>
# Favorite colors: [7, 33, 99]
# Favorite colors: 7, 33, 99


def my_generator():
    for i in range(10):
        yield i

def my_func(*args):
    print(args)

it = my_generator()
my_func(*it)
# 1) change to tuple : risk to large data => generator with * causes shortage of memory
# 2) can't add new potional arg without changing code  => causes bugs
# >>>
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)


def log3(sequence, message, *values):
    if not values:
        print('%s: %s' % (sequence, message))
    else:
        values_str = ', '.join(str(x) for x in values)
        print('%s: %s: %s' % (sequence, message, values_str))

log3(1, 'Favorites', 7, 33) # new usage is okay
log3('Favorites', 7, 33) # old not okay
# >>>
# 1: Favorites: 7, 33
# Favorites: 7: 33