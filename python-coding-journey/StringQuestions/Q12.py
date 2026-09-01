# 12. Check palindrome string
str1=input("Enter a string: ")

reverse=""
for i in str1:
    reverse=i+reverse

if(reverse==str1):
    print(str1, " is palindrome.")
else:
    print(str1, " is not a palindrome.")

