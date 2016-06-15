
for i in range(3):
    print('Loop %d' % i)
else:
    print('Else block!')
# >>>
# Loop 0
# Loop 1
# Loop 2
# Else block!

for i in range(3):
    print('Loop %d' % i)
    if i == 1:
        break
else:
    print('Else block!')
# >>>
# Loop 0
# Loop 1

for x in []:
    print('Never runs')
else:
    print('For Else block')

while False:
    print('Never runs')
else:
    print('While Else block')
# >>>
# For/While Else block

a = 4
b = 9
for i in range(2, min(a, b) + 1):
    print('Testing', i)
    if a % i == 0 and b % i == 0:
        print('Not coprime')
        break
else:
    print('Coprime')
# >>>
# Testing 2
# Testing 3
# Testing 4
# Coprime

def corprime(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True

def corprime2(a, b):
    is_corprime = True
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            is_corprime = False
            break
    return is_corprime

print(corprime(4, 9))
# >>>
# True