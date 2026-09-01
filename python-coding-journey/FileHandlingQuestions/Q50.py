# 50. Count lines in file
with open("sample.txt", "r") as file:
    count = len(file.readlines())

print("Total Lines:", count)