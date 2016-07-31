
def insertion_sort(data):
    result = []
    for value in data:
        insert_value(result, value)
    return result

def insert_value(array, value):
    for i, existing in enumerate(array):
        if existing > value:
            array.insert(i, value)
            return
    array.append(value)


from random import randint


max_size = 10**4
data = [ randint(0, max_size) for _ in range(max_size) ]
test = lambda: insertion_sort(data)


# cProfile (C extenstion) is better than profile (pure python)
from cProfile import Profile


profiler = Profile()
profiler.runcall(test)


from sys import stdout as STDOUT
from pstats import Stats

stats = Stats(profiler, stream=STDOUT)
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats()
# >>>
#          20003 function calls in 2.077 seconds

#    Ordered by: cumulative time

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    2.077    2.077 58_profile_before_optimization.py:21(<lambda>)
#         1    0.003    0.003    2.077    2.077 58_profile_before_optimization.py:2(insertion_sort)
#     10000    2.060    0.000    2.074    0.000 58_profile_before_optimization.py:8(insert_value)
#      9991    0.014    0.000    0.014    0.000 {method 'insert' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         9    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# ncalls: the number of function calls
# tottime: time for runing a function
# tottime percall: avg time for calling a function ( = tottime / ncalls )
# cumtime: cumulative time for running a function including other function calls
# cumtime percall: avg cumtime for calling a function  ( = cumtime / ncalls)


from bisect import bisect_left

# ref: 46_built-in_data_structure_algorithm.py
def insert_value(array, value):
    i = bisect_left(array, value)
    array.insert(i, value)


profiler = Profile()
profiler.runcall(test)
stats = Stats(profiler, stream=STDOUT)
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats()
# >>>
#          30003 function calls in 0.022 seconds

#    Ordered by: cumulative time

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.022    0.022 58_profile_before_optimization.py:21(<lambda>)
#         1    0.002    0.002    0.022    0.022 58_profile_before_optimization.py:2(insertion_sort)
#     10000    0.004    0.000    0.020    0.000 58_profile_before_optimization.py:61(insert_value)
#     10000    0.012    0.000    0.012    0.000 {method 'insert' of 'list' objects}
#     10000    0.005    0.000    0.005    0.000 {built-in method _bisect.bisect_left}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def my_utility(a, b):
    c = 1
    for i in range(100):
        c += a * b

def first_func():
    for _ in range(1000):
        my_utility(4, 5)

def second_func():
    for _ in range(10):
        my_utility(1, 3)

def my_program():
    for _ in range(20):
        first_func()
        second_func()

profiler = Profile()
profiler.runcall(my_program)
stats = Stats(profiler, stream=STDOUT)
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats() # hard to understand
# >>>
#          20242 function calls in 0.213 seconds

#    Ordered by: cumulative time

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.213    0.213 58_profile_before_optimization.py:99(my_program)
#        20    0.005    0.000    0.211    0.011 58_profile_before_optimization.py:91(first_func)
#     20200    0.207    0.000    0.207    0.000 58_profile_before_optimization.py:86(my_utility)
#        20    0.000    0.000    0.002    0.000 58_profile_before_optimization.py:95(second_func)
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


stats.print_callers()
# >>>
#    Ordered by: cumulative time

# Function                                           was called by...
#                                                        ncalls  tottime  cumtime
# 58_profile_before_optimization.py:99(my_program)   <-
# 58_profile_before_optimization.py:91(first_func)   <-      20    0.004    0.197  58_profile_before_optimization.py:99(my_program)
# 58_profile_before_optimization.py:86(my_utility)   <-   20000    0.192    0.192  58_profile_before_optimization.py:91(first_func)
#                                                           200    0.002    0.002  58_profile_before_optimization.py:95(second_func)
# 58_profile_before_optimization.py:95(second_func)  <-      20    0.000    0.002  58_profile_before_optimization.py:99(my_program)
# {method 'disable' of '_lsprof.Profiler' objects}   <-