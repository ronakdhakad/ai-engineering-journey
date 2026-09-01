# 30. Find maximum occurring element
list1=[1,2,4,6,8,2,4,2]

max_element=list1[0]
max_count=list1.count(list1[0])
for i in list1:
    if list1.count(i)>max_count:
        max_count=list1.count(i)
        max_element=i

print("Maximum occurring element:",max_element)
print("Frequency:",max_count)