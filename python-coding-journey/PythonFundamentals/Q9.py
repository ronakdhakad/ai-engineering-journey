# 9. Reverse a number

a = int(input("Enter a number: "))
b=0
print(a)
while(a!=0):
    b=b*10
    b=b+(a%10)
    a=int(a/10)

print(b)

num = input("Enter a number: ")
print("Reversed number =", num[::-1])