# 22. Find second largest element
lst=list(map(int,(input("Enter list items: ").split())))

largest=float('-inf')
Secondlargest=float('-inf')
for item in lst:
    if(largest<item):
        Secondlargest=largest
        largest=item
    elif(largest!=item and Secondlargest<item):
        Secondlargest=item

print(largest)
print(Secondlargest)