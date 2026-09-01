# Check whether a string is a palindrome

s=input("Enter a string: ")

left=0
right=len(s)-1
check=True
while(left<right):
    if(s[left]!=s[right]):
        check=False
        break
    left+=1
    right-=1

if(check):
    print(s+ " is a palindrome..")
else:
    print(s+ " is not a palindrome..")