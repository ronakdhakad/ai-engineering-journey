# 6. Calculate factorial of a number

a=int(input("Enter a fact num: "))
fact=1
while(a!=0):
    fact*=a
    a-=1
print(fact)