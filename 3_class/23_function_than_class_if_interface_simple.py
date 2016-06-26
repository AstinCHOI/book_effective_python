
names = ['Socrates', 'Archimedes', 'Plato', 'Aristotle']
names.sort(key=lambda x: len(x))
print(names)
# >>>
# ['Plato', 'Socrates', 'Aristotle', 'Archimedes']


def log_missing():
    print('Key added')
    return 0

current = {'green': 12, 'blue': 3}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9),
]
import collections
result = collections.defaultdict(log_missing, current)
print('Before: ', dict(result))
for key, amount in increments:
    result[key] += amount
print('After: ', dict(result))
# >>>
# Before:  {'blue': 3, 'green': 12}
# Key added
# Key added
# After:  {'blue': 20, 'orange': 9, 'green': 12, 'red': 5}


def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count # status preserve closure
        added_count += 1
        return 0
    
    result = collections.defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount
    
    return result, added_count

result, count = increment_with_report(current, increments)
assert count == 2


class CountMissing(object):
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0

counter = CountMissing()
result = collections.defaultdict(counter.missing, current)

for key, amount in increments:
    result[key] += amount

assert counter.added == 2


class BetterCountMissing(object):
    def __init__(self):
        self.added = 0
    
    def __call__(self):
        self.added += 1
        return 0

counter = BetterCountMissing()
counter()
assert callable(counter)

counter = BetterCountMissing()
result = collections.defaultdict(counter, current)
for key, amount in increments:
    result[key] += amount
assert counter.added == 2