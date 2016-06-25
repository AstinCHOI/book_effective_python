
names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]
print(letters)
# >>>
# [7, 4, 5]

longest_name = None
max_letters = 0

for i in range(len(names)):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count

for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = name
        max_letters = count

# In python3, 2 or more iterators with lazy generator
# In python2, it's a not genorator
# so, use izip from itertools
for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count

print(longest_name)

# keeps yielding tuples until a wrapped iterator is exhausted
names.append('Rosalind')
for name, count in zip(names, letters):
    print(name)
# >>>
# Cecilia
# Lise
# Marie

import sys
if sys.version_info[0] >= 3:
    from itertools import zip_longest 
else:
    from itertools import izip_longest as zip_longest
for name, count in zip_longest(names, letters):
    print(name)
# >>>
# Rosalind