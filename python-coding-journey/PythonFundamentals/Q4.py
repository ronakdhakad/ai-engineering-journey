# 4. Find the largest of three numbers
a=int(input("Enter a num1: "))
b=int(input("Enter a num2: "))
c=int(input("Enter a num3: "))

if(a>b and a>c):
    print(a, " is largest")
elif(b>a and b>c):
    print(b, " is largest")
else:
    print(c, " is largest")