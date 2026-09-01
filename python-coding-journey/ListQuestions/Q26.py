# 26. Rotate array by K positions

lst = list(map(int,(input("Enter numbers: ").split())))

k=2
# Left Rotation
# for i in range(k):
#     first=lst.pop(0)
#     lst.append(first)

# print(lst)

# Right Rotation

for i in range(k):
    last=lst.pop()
    lst.insert(0,last)

print(lst)