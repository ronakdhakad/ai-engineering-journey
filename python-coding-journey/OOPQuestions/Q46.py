# 46. Create Abstract Class
# An Abstract Class is a class that cannot be instantiated directly and may contain abstract methods that must be implemented by child classes.

# In Python, abstract classes are created using the abc module.
# from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        print("Area called...!")

class circle(shape):
    def area(self):
        print("Circle called...!")


c=circle()
c.area()