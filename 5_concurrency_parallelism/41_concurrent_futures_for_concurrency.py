
def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

numbers = [(1963309, 2265973), (2030677, 3814172),
           (1551645, 2229620), (2039045, 2020802)]
from time import time
start = time()
results = list(map(gcd, numbers))
end = time()
print('Took %.3f seconds' % (end - start))
# >>>
# Took 1.103 seconds


from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
start = time()
pool = ThreadPoolExecutor(max_workers=2) # overhead for creating thread pool
results = list(pool.map(gcd, numbers))
end = time()
print('Took %.3f seconds' % (end - start))
# >>>
# Took 1.186 seconds


start = time()
pool = ProcessPoolExecutor(max_workers=2) # The one change
results = list(pool.map(gcd, numbers))
end = time()
print('Took %.3f seconds' % (end - start))
# >>>
# Took 0.677 seconds


# isolated and high-leverage jobs for ProcessPoolExecutor

# Try first concurrent.futures (ProcessPoolExecutor uses multiprocessing)
# Second advanced multiprocessing functions 
# Lastly, C extension module like http://cython.org/ and http://numba.pydata.org/