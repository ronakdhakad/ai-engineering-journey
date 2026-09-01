# 14. Find character frequency

str=input("Enter a string: ")

freq={}
for char in str:
    if char in freq:
        freq[char]=freq[char]+1
    else:
        freq[char]=1



for char in freq:    
    print(char," ", freq[char])