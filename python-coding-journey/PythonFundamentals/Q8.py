# 8. Check whether a number is prime

a = int(input("Enter a number: "))

b= True

for i in range(2,int(a/2)+1):
    if(a%i==0):
        b=False
        break
if(b):
    print(a," is a prime number")
else:
    print(a," is not a prime number")
    