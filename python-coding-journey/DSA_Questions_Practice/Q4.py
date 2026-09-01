# Check whether two strings are anagrams

s1=input("Enter a string1: ")
s2=input("Enter a string2: ")

def is_anagram(s1,s2):
    if(len(s1)!=len(s2)):
        return False

    freq={}

    for ch in s1:
        if(ch in freq):
            freq[ch]+=1
        else:
            freq[ch]=1

    for ch in s2:
        if(ch not in freq):
            return False

        freq[ch]-=1
    
        if(freq[ch]<0):
            return False
    
    return True

if(is_anagram(s1,s2)):
    print("String are an anagram: ")
else:
    print("String are not an anagram: ")