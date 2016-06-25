
def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)
# >>>
# [11.538461538461538, 26.923076923076923, 61.53846153846154]


def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)

it = read_visits('../example/my_numbers.txt')
percentages = normalize(it)
print(percentages)
# >>>
# []


it = read_visits('../example/my_numbers.txt')
print(list(it))
print(list(it)) # already consumed
# >>>
# [15, 35, 80]
# []


def normalize_copy(numbers):
    numbers = list(numbers) # copy iterator
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

it = read_visits('../example/my_numbers.txt')
percentages = normalize_copy(it)
print(percentages)
# >>>
# [11.538461538461538, 26.923076923076923, 61.53846153846154]


def normalize_func(get_iter):
    total = sum(get_iter()) # new iterator
    result = []
    for value in get_iter(): # new iterator
        percent = 100 * value / total
        result.append(percent)
    return result

percentages = normalize_func(lambda: read_visits('../example/my_numbers.txt'))
print(percentages)
# >>>
# [11.538461538461538, 26.923076923076923, 61.53846153846154]


class ReadVisits(object): # iterable container class
    def __init__(self, data_path):
        self.data_path = data_path
    
    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)

visits = ReadVisits('../example/my_numbers.txt')
percentages = normalize(visits)
print(percentages)
# >>>
# [11.538461538461538, 26.923076923076923, 61.53846153846154]


# iter(iterator) returns iterator itself
# iter(container_type) returns new iterator
def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers): # iterator -- deny!
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

visits = [15, 35, 80]
normalize_defensive(visits)
visits = ReadVisits('../example/my_numbers.txt')
normalize_defensive(visits)
# >>>
# [11.538461538461538, 26.923076923076923, 61.53846153846154]
# [11.538461538461538, 26.923076923076923, 61.53846153846154]

it = iter(visits)
normalize_defensive(it)
# >>>
# TypeError: Must supply a container