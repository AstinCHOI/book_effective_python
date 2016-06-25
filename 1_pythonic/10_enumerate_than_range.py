
import random

random_bits = 0
for i in range(64):
    if random.randint(0, 1):
        random_bits |= 1 << i

print(random_bits)
# >>>
# 17444800564200968726

flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for flavor in flavor_list:
    print('%s is delicious' % flavor)
# >>>
# vanilla is delicious
# chocolate is delicious
# pecan is delicious
# strawberry is delicious

for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print('%d: %s' % (i+1, flavor))

for i, flavor in enumerate(flavor_list):
    print('%d: %s' % (i+1, flavor))

for i, flavor in enumerate(flavor_list, 1):
    print('%d: %s' % (i, flavor))
# >>>
# 1: vanilla
# 2: chocolate
# 3: pecan
# 4: strawberry

