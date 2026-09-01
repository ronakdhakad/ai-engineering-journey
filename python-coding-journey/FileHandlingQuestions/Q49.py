# 49. Read file and count words
file = open("sample.txt", "r")

data = file.read()

words = data.split()

print("Total Words:", len(words))

file.close()