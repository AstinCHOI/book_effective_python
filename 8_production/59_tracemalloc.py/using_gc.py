
import gc
found_objects = gc.get_objects()
print('%d objects before' % len(found_objects))

import waste_memory
x = waste_memory.run()
found_objects = gc.get_objects()
print('%d objects before' % len(found_objects))
for obj in found_objects[:3]:
    print(repr(obj)[:100])
# >>>
# 6280 objects before
# 16947 objects before
# <waste_memory.MyObject object at 0x1028003c8>
# <waste_memory.MyObject object at 0x102800400>
# <waste_memory.MyObject object at 0x102800438>