# 53. Count occurrences of a word in file

with open("sample.txt", "r") as file:
    data = file.read().lower()

word = input("Enter word to search: ").lower()

words = data.split()

count = words.count(word)

print("Occurrences:", count)