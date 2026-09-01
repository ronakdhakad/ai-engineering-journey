# 57. Create login system using exceptions

class InvalidLoginException(Exception):
    pass

username = "admin"
password = "1234"

try:
    user = input("Enter Username: ")
    pwd = input("Enter Password: ")

    if user != username or pwd != password:
        raise InvalidLoginException("Invalid Username or Password")

    print("Login Successful")

except InvalidLoginException as e:
    print(e)