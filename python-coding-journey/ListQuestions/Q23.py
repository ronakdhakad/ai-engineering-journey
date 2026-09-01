# 23. Remove duplicates from list
lst=list(map(int,(input("Enter list items: ").split())))

newlist=[]

for num in lst:
    if num not in newlist:
        newlist.append(num)
print(newlist)

