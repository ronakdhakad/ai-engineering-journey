# 16. Check whether two strings are anagrams


str1 = input("Enter a String: ")


str2 = input("Enter a String: ")

if sorted(str1.lower())==sorted(str2.lower()):
    print(str1," and ", str2," are anagrams")
else:
    print(str1," and ", str2," not an anagrams")