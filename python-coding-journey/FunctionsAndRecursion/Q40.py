# 40. Sum of digits using recursion

num = int(input("Enter a number: "))

def sum_digit(num):
    if num==0:
        return 0
    
    return (num%10)+sum_digit(num//10)

print("Sum of digits =", sum_digit(num))