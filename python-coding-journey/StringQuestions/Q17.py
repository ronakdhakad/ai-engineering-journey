# 17. Find first non-repeated character
s = input("Enter a string: ")

freq = {}
# freq.get(ch, 0) + 1
# Count frequency of each character

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# Find first non-repeated character
for ch in s:
    if freq[ch] == 1:
        print("First non-repeated character:", ch)
        break
else:
    print("No non-repeated character found")