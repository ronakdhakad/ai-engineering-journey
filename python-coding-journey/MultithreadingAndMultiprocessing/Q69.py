# # 69. Producer Consumer Problem
# The Producer-Consumer Problem is a synchronization problem where:
# Producer creates data and puts it into a shared buffer (queue).
# Consumer takes data from the buffer and processes it.
# A Lock or Queue is used to avoid conflicts between threads.

import threading

buffer = []
lock = threading.Lock()

def producer():
    for i in range(1, 6):
        with lock:
            buffer.append(i)
            print("Produced:", i)

def consumer():
    for i in range(1, 6):
        while True:
            with lock:
                if buffer:
                    item = buffer.pop(0)
                    print("Consumed:", item)
                    break

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()

t1.join()
t2.join()