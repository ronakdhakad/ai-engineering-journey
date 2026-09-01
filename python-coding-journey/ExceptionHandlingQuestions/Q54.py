# 54. Division by zero handling

try:
    a=int(input())
    b=int(input())
    c=a/b
    print(c)
except ZeroDivisionError as e:
    print("Exception occured...",e)
except Exception as e:
    print("Exception occured...",e)
finally:
    print("Finally executed..")
