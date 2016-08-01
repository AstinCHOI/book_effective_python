
# from python 3.4
import tracemalloc
tracemalloc.start(10)

time1 = tracemalloc.take_snapshot()
import waste_memory
x = waste_memory.run()
time2 = tracemalloc.take_snapshot()
stats = time2.compare_to(time1, 'traceback')
top = stats[0]
print('\n'.join(top.traceback.format()))
# >>>
#   File "../8_production/59_tracemalloc.py/waste_memory.py", line 7
#     self.x = os.urandom(100)
#   File "../8_production/59_tracemalloc.py/waste_memory.py", line 13
#     obj = MyObject()
#   File "../8_production/59_tracemalloc.py/waste_memory.py", line 20
#     deep_values.append(get_data())
#   File "with_trace.py", line 8
#     x = waste_memory.run()