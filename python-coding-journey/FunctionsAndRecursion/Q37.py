# 37. Fibonacci using recursion
def fibo(a, b,limit):
    if limit==0:
        return

    print(a, end=" ")
    fibo(b, a + b,limit-1)

fibo(0, 1,10)


a=b
b=a+b

