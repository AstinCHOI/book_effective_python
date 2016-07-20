
# double-ended queue
from collections import deque
fifo = deque()
fifo.append(1) # producer
x = fifo.popleft() # consumer

