
a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = a[::2]
evens = a[1::2]
print(odds)
print(evens)
# >>>
# ['red', 'yellow', 'blue']
# ['orange', 'green', 'purple']

x = b'mongoose'
y = x[::-1]
print(y)
# >>>
# b'esoognom'

w = '바보'
x = w.encode('utf-8')
y = x[::-1]
try:
    z = y.decode('utf-8')
except UnicodeDecodeError as e:
    print(e)

# Hard to read    
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(a[::2])
print(a[::-2])
print(a[2::2])
print(a[-2::-2])
print(a[-2:2:-2])
print(a[2:2:-2])
# ['a', 'c', 'e', 'g']
# ['h', 'f', 'd', 'b']
# ['c', 'e', 'g']
# ['g', 'e', 'c', 'a']
# ['g', 'e']
# []

# Use like this
b = a[::2] # Use + stride if possible 
c = b[1:-1] # then slicing
print(b)
print(c)
# >>>
# ['a', 'c', 'e', 'g']
# ['c', 'e']