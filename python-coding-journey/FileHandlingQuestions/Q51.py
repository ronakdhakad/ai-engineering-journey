# 51. Find longest word from file

with open("sample.txt", "r") as file:
    data = file.read()

words = data.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)