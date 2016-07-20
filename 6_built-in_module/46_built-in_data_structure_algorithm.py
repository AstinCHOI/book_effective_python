
# 1) double-ended queue
# faster than list for first item adding/removing operation
from collections import deque
fifo = deque()
fifo.append(1) # producer
x = fifo.popleft() # consumer


# 2) soreted dictionary
import random
a = {}
a['foo'] = 1
a['bar'] = 2

# cause hash crash by adding data to 'b'
while True:
    z = random.randint(99, 1013)
    b = {}
    for i in range(z):
        b[i] = i
    b['foo'] = 1
    b['bar'] = 2
    for i in range(z):
        del b[i]
    if str(b) != str(a):
        break

print(a)
print(b)
print('Equal?', a == b)
# >>>
# {'foo': 1, 'bar': 2}
# {'bar': 2, 'foo': 1}
# ('Equal?', True)

from collections import OrderedDict
a = OrderedDict()
a['foo'] = 1
a['bar'] = 2

b = OrderedDict()
b['foo'] = 'red'
b['bar'] = 'blue'

for val1, val2 in zip(a.values(), b.values()):
    print(val1, val2)
# >>>
# 1 red
# 2 blue


# 3) default dictionary
stats = {}
key = 'my_counter'
if key not in stats:
    stats[key] = 0
stats[key] += 1

# vs

from collections import defaultdict
stats = defaultdict(int)
stats['my_counter'] += 1


# 4) heap queue (priority queue)
from heapq import heappush, heappop, nsmallest

a = []
heappush(a, 5)
heappush(a, 3)
heappush(a, 7)
heappush(a, 4)

print(heappop(a), heappop(a), heappop(a), heappop(a))
# >>>
# 3 4 5 7

a = []
heappush(a, 5)
heappush(a, 3)
heappush(a, 7)
heappush(a, 4)
assert a[0] == nsmallest(1, a)[0] == 3
print('Before:', a)
a.sort()
print('After:', a) # even using sort, "a" keeps heap
# >>>
# Before: [3, 4, 7, 5]
# After: [3, 4, 5, 7]


# 5) bisection
x = list(range(10**6))
i = x.index(991234) # liner time

from bisect import bisect_left
i = bisect_left(x, 991234)


from timeit import timeit
print(timeit(
    'a.index(len(a)-1)',
    'a = list(range(100))',
    number=1000))
print(timeit(
    'bisect_left(a, len(a)-1)',
    'from bisect import bisect_left;'
    'a = list(range(10**6))',
    number=1000))
# >>>
# 0.0018228629996883683
# 0.0014346809984999709


# 6) itertools
# help(itertools)

# link interators together
# chain: combines into a single iterator
# cycle: repeats forever
# tee: splits one into multiple parallel
# zip_longest: A variant of the zip built-in function of different lengths

# item filtering
# islice: slices an iterator by numerical indexes without copying
# takewhile: returns items from an iterator while a predicate function returns True
# dropwhile: returns items form an iterator once the predicate function returns False for the first time
# filterfalse: returns all items from an iterator where a predicate function returns False. The opposite of the filter built-in function

# item combination
# product: Return the Cartesian product of items from an iterator, which is a nice alternative to deeply nested list comprehensions.
# permutation: returns ordered permutations of length N with items from an iterator
# combination: returns the unordered combinations of length N with unrepeated items from an iterator.