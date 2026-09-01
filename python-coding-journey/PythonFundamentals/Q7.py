# 7. Generate Fibonacci series
a = int(input("Enter a size of series: "))

n=0
m=1
while(a!=0):
    print(n," ")
    n=n+m
    m=n-m
    a-=1
