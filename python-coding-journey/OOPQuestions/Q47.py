# 47. Demonstrate Multiple Inheritance
# Multiple Inheritance means a class inherits from more than one parent class.
class Father:
    def father_method(self):
        print("Father Method")

class Mother:
    def mother_method(self):
        print("Mother Method")

class Child(Father, Mother):
    def child_method(self):
        print("Child Method")

c = Child()

c.father_method()
c.mother_method()
c.child_method()