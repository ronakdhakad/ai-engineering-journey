# 20. Find longest word in a sentence

sentence = input("Enter a Sentence: ")

words=sentence.split()

longest=""
for word in words:
    if(len(longest)<len(word)):
        longest=word

print("Longest word: ",longest)