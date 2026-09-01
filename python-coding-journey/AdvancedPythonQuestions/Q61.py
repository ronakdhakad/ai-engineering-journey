# 61. Create custom Decorator
# A Decorator is a function that modifies the behavior of another function without changing its code.

def my_decorater(func):

    def wrapper():
        print("after..")
        func()
        print("before..")

    return wrapper

@my_decorater
def greet():
    print("Hello..")

greet()