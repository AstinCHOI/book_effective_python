
# from python 3.4
import tracemalloc
tracemalloc.start(10) # save stack frame for maximum 10

time1 = tracemalloc.take_snapshot()
import waste_memory
x = waste_memory.run()
time2 = tracemalloc.take_snapshot()

stats = time2.compare_to(time1, 'lineno')
for stat in stats[:3]:
    print(stat)
# >>>
# ../59_tracemalloc.py/waste_memory.py:7: size=2235 KiB (+2235 KiB), count=29985 (+29985), average=76 B
# ../59_tracemalloc.py/waste_memory.py:8: size=869 KiB (+869 KiB), count=10000 (+10000), average=89 B
# ../59_tracemalloc.py/waste_memory.py:13: size=547 KiB (+547 KiB), count=10000 (+10000), average=56 B