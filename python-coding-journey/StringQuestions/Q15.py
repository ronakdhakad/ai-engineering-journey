# 15. Remove duplicate characters

str = input("Enter a String: ")

result=""
for char in str:
    if char not in result:
        result+=char
    

print(str)
print(result)