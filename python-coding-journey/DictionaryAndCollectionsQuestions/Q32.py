# 32. Group words by length

words = ['apple','banana','cat','car','dog','camal']

result={}
for word in words:
    if len(word) in result:
        result[len(word)].append(word)
    else:
        result[len(word)]=[word]

print(result)
