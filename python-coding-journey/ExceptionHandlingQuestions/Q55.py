# 55. Custom Exception
# Example:
# InsufficientBalanceException
# A custom exception is a user-defined exception created by inheriting from Python's Exception class.
class InsufficientBalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceException("Insufficient Balance")

        self.balance -= amount
        print("Remaining Balance:", self.balance)

a = BankAccount(1000)

try:
    a.withdraw(1500)
except InsufficientBalanceException as e:
    print(e)