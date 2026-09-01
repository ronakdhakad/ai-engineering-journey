# 39. Power of number using recursion

num = int(input("Enter a number: "))
expo = int(input("Enter exponent: "))
def power(num,expo):
    if(expo==0):
        return 1

    return num*power(num,expo-1)

print("Result =", power(num, expo))
