# 68. Demonstrate Lock usage
# A Lock is used to prevent multiple threads from accessing the same resource at the same time (thread synchronization).
import threading

lock = threading.Lock()

def display(name):
    with lock:
        for i in range(3):
            print(name)

t1 = threading.Thread(target=display, args=("Thread-1",))
t2 = threading.Thread(target=display, args=("Thread-2",))

t1.start()
t2.start()

t1.join()
t2.join()