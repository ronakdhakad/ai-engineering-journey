# 42. Implement Bank Account class

# Features:

# Deposit
# Withdraw
# Check Balance

class Account:
    def __init__ (self):
        self.balance=0

    def withdraw(self,amount):
        if(self.balance>=amount):
            self.balance-=amount
    
    def deposit(self,amount):
        if(amount>0):
           self.balance+=amount

    def check_balance(self):
        print("Balance: ",self.balance) 

a=Account()

a.deposit(int(input("Enter a deposit amount: ")))
a.withdraw(int(input("Enter a deposit amount: ")))

a.check_balance()


