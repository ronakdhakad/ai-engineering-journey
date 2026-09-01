# Find the first non-repeating character in a string

s=input("Enter a string: ")


freq={}
for char in s:
    if(char in freq):
        freq[char]=freq[char]+1
    else:
        freq[char]=1

for char in freq:
    if freq[char]==1:
        print("first non-repeating character: ",char)
        break