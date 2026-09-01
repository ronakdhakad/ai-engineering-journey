# Find the frequency of every character in a string
s2=input("Enter a string2: ")

def frequency(s):
    freq={}

    for ch in s:
        if(ch==" "):
            continue
            
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1

    for ch in freq:
        print(ch," - ",freq[ch])

frequency(s2)