# 18. String compression
# aaabbcc = a3b2c2

s = input("Enter a string: ")

string=""
freq={}
for char in s:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1

for char in freq:
    string=string+char+str(freq[char])

print(string)