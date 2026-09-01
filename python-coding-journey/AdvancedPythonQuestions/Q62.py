# 62. Create logging Decorator
# A logging decorator logs (prints) information whenever a function is called.

def logger(func):

    def wrapper():
        print("Function", func.__name__, "is called")
        func()

    return wrapper


@logger
def greet():
    print("Hello World")

greet()