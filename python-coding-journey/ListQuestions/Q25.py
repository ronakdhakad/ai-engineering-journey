# 25. Find common elements between two lists
lst1 = list(map(int,(input("Enter numbers: ").split())))

lst2 = list(map(int,(input("Enter numbers: ").split())))

comman=[]
for num in lst1:
    if num in lst2:
        comman.append(num)

print(list(set(comman)))