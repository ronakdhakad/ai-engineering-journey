# 67. Calculate factorial using multiprocessing
# The multiprocessing module allows Python to run tasks in separate processes.
from multiprocessing import Process

def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    print("Factorial =", fact)

num = int(input("Enter a number: "))

p = Process(target=factorial, args=(num,))

p.start()
p.join()