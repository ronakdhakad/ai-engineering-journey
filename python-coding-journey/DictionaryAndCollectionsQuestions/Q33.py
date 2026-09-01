# 33. Find most common word in paragraph
string = input("Enter a paragraph: ")

words=string.split()

result={}

for word in words:
    if word in result:
        result[word]+=1
    else:
        result[word]=1

max_word=max(result,key=result.get)
print(max_word)
print(result[max_word])