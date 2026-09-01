# 19. Count words in a sentence
sentence = input("Enter a Sentence: ")

count=0
# for char in sentence:
#     if(char == " "):
#         count+=1

for char in sentence:
    if " " in char:
        count+=1 

print("Words: ",count+1)

sentence1 = input("Enter a sentence: ")

words = sentence1.split()

print("Number of words:", len(words))