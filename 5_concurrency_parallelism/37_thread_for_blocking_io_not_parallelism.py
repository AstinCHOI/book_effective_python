
import time
def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i

numbers = [2139079, 121479, 1516637, 1852285]
start = time.time()
for number in numbers:
    list(factorize(number))
end = time.time()
print('Took %.3f seconds' % (end - start))
# >>>
# Took 0.797 seconds


from threading import Thread

class FactorizeThread(Thread):
    def __init__(self, number):
        super(FactorizeThread, self).__init__()
        self.number = number
    
    def run(self):
        self.factors = list(factorize(self.number))

start = time.time()
threads = []
for number in numbers:
    thread = FactorizeThread(number)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
end = time.time()
print('Took %.3f secnods' % (end - start))
# >>>
# Took 1.014 secnods


import select
 
def slow_systemcall():
    select.select([], [], [], 0.1)

start = time.time()
for _ in range(5):
    slow_systemcall()
end = time.time()
print('Took %.3f secnods' % (end - start))
# >>>
# Took 0.514 secnods


start = time.time()
threads = []
for _ in range(5):
    thread = Thread(target=slow_systemcall)
    thread.start()
    threads.append(thread)

def compute_helicopter_location(index):
    pass

for i in range(5):
    compute_helicopter_location(i)
for thread in threads:
    thread.join()
end = time.time()
print('Took %.3f secnods' % (end - start))
# >>>
# Took 0.106 secnods


# Python threads can't run bytecode in parallel on multiple CPU cores because of the global interpreter lock (GIL)
# Python threads are still useful despite the GIL because they provide an easy way to do multiple things at seemingly the same time.
# Use Python threads to make multiple system calls in parallel. This allows you to do blocking I/O at the same tiem as computation.
