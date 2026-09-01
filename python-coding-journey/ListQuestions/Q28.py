# 28. Merge two sorted lists

list1 = list(map(int,(input("Enter numbers: ").split())))

list2 = list(map(int,(input("Enter numbers: ").split())))

list1.sort()
list2.sort()
merge=list1+list2
print(sorted(merge))
for items in list1:
    list2.append(items)

print(list2)