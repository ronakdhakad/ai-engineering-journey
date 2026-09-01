# 52. Copy contents from one file to another
with open("source.txt", "r") as source:
    data = source.read()

with open("destination.txt", "w") as destination:
    destination.write(data)

print("File copied successfully")