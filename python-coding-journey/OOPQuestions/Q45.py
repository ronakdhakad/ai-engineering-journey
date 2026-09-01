# 45. Demonstrate Encapsulation
# Encapsulation means binding data (variables) and methods together in a class and restricting direct access to data.

# In Python, encapsulation is commonly demonstrated using private variables (__variable).

class Student:
    def __init__(self):
        self.__marks = 0      # Private variable

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks


s = Student()

s.set_marks(85)

print("Marks:", s.get_marks())