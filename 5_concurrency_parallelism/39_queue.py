
from collections import deque
from threading import Thread, Lock
import time
class MyQueue(object):
    def __init__(self):
        self.items = deque()
        self.lock = Lock()

    def put(self, item):
        with self.lock:
            self.items.append(item)

    def get(self):
        with self.lock:
            return self.items.popleft()

class Worker(Thread):
    def __init__(self, func, in_queue, out_queue):
        super(Worker, self).__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.polled_count = 0
        self.work_done = 0

    def run(self):
        while True:
            self.polled_count += 1
            try:
                item = self.in_queue.get()
            except IndexError:
                time.sleep(0.01) # nothing to handle
            except AttributeError:
                # The magic exit signal
                return
            else:
                result = self.func(item)
                self.out_queue.put(result)
                self.work_done += 1

def download(item):
    return item

def resize(item):
    return item

def upload(item):
    return item

download_queue = MyQueue()
resize_queue = MyQueue()
upload_queue = MyQueue()
done_queue = MyQueue()
threads = [
    Worker(download, download_queue, resize_queue),
    Worker(resize, resize_queue, upload_queue),
    Worker(upload, upload_queue, done_queue)
]

for thread in threads:
    thread.start()
for _ in range(1000):
    download_queue.put(object())

while len(done_queue.items) < 1000:
    # Do something useful while waiting
    time.sleep(0.1)

# Stop all the threads by causing an exception in their run methods.
for thread in threads:
    thread.in_queue = None

processed = len(done_queue.items)
polled = sum(t.polled_count for t in threads)
print('Processed', processed, 'items after polling', polled, 'times')
# >>>
# Processed 1000 items after polling 3025 times

# 3 problems 
# 1) must wait until done_queue stacked
# 2) constantly run "run" method of Worker (no way to signal at loop to escape)
# 3) if pipeline is stagnated


# Queue: remove busy waiting which continuously checks by get method
from queue import Queue
queue = Queue()

def consumer():
    print('Customer waiting')
    queue.get() # run after put()
    print('Customer done')

thread = Thread(target=consumer)
thread.start()

print('Producer putting')
queue.put(object()) # run before get()
thread.join()
print('Producer done')
# >>>
# Customer waiting
# Producer putting
# Customer done
# Producer done


queue = Queue(1)

def consumer():
    time.sleep(0.1)
    queue.get()
    print('Consumer got 1')
    queue.get()
    print('Consumer got 2')

thread = Thread(target=consumer)
thread.start()

queue.put(object())
print('Producer put 1')
queue.put(object())
print('Producer put 2')
thread.join()
print('Producer done')
# >>>
# Producer put 1
# Consumer got 1
# Producer put 2
# Consumer got 2
# Producer done


in_queue = Queue()
def consumer():
    print('Consumer waiting')
    work = in_queue.get()
    print('Cousumer working')
    # Doing work
    print('Consumer done')
    in_queue.task_done()

Thread(target=consumer).start()

in_queue.put(object())
print('Producer waiting')
in_queue.join()
print('Producer done')
# >>>
# Consumer waiting
# Producer waiting
# Cousumer working
# Consumer done
# Producer done


class ClosableQueue(Queue):
    SENTINEL = object()

    def close(self):
        self.put(self.SENTINEL)

    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.SENTINEL:
                    return # Cause the thread to exit
                yield item
            finally:
                self.task_done()

class StoppableWorker(Thread):
    def __init__(self, func, in_queue, out_queue):
        super(StoppableWorker, self).__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue

    def run(self):
        for item in self.in_queue:
            result = self.func(item)
            self.out_queue.put(result)

download_queue = ClosableQueue()
resize_queue = ClosableQueue()
upload_queue = ClosableQueue()
done_queue = ClosableQueue()
threads = [
    StoppableWorker(download, download_queue, resize_queue),
    StoppableWorker(resize, resize_queue, upload_queue),
    StoppableWorker(upload, upload_queue, done_queue),
]

for thread in threads:
    thread.start()
for _ in range(1000):
    download_queue.put(object())

download_queue.close()
download_queue.join()
resize_queue.close()
resize_queue.join()
upload_queue.close()
upload_queue.join()
print(done_queue.qsize(), 'items finished')
# >>>
# 1000 items finished