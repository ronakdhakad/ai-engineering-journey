# 56. Multiple exception handling
# Multiple Exception Handling means handling more than one type of exception using multiple except blocks.
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter valid numbers")