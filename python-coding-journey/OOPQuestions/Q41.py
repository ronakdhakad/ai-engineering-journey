# 41. Create Student class
# Attributes:
# id
# name
# marks
# Methods:
# display()

class Student:

    def __init__(self,id,name,mark):
        self.ids=id
        self.names=name
        self.marks=mark

    def display(self):
        print("ID: ",self.ids)
        print("Name: ",self.names)
        print("Marks: ",self.marks)

id=int(input("Enter ID: "))
name=(input("Enter Name: "))
marks=int(input("Enter Marks: "))

s=Student(id,name,marks)
s.display()