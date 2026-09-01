# 21. Find largest element in a list
lst=list(map(int,(input("Enter list items: ").split())))

largest=lst[0]
print(largest)
for item in lst:
    if(largest<item):
        largest=item
print(largest)