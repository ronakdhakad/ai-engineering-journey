# 48. Employee Management System

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)


emp_id = int(input("Enter Employee ID: "))
name = input("Enter Employee Name: ")
salary = float(input("Enter Salary: "))

e1 = Employee(emp_id, name, salary)

print("\nEmployee Details")
e1.display()