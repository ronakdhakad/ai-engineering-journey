# 13. Count vowels and consonants

str=input("Enter a string: ")
str.lower()
vowels=0
consonants=0

for char in str:
    if(char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
        vowels+=1
    else:
        consonants+=1

print("vowels: ",vowels)
print("consonants: ",consonants)
