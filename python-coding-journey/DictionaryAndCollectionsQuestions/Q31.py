# 31. Count frequency of elements using Counter

from collections import Counter

lst= list(map(int,(input("Enter the numbers: ").split())))

print(Counter(lst))


list1 = [1, 2, 4, 6, 8, 2, 4, 2]

freq = Counter(list1)

for key, value in freq.items():
    print(key, ":", value)