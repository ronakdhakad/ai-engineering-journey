# 65. Print numbers using multiple threads

import threading

class MyThread(threading.Thread):

    def run(self):
        for i in range(1,6):
            print(i)


t=MyThread()

t.start()
t.join()


def print_numbers():
    for i in range(1, 6):
        print(i)

t1 = threading.Thread(target=print_numbers)

t1.start()
t1.join()