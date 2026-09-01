# 29. Find duplicate elements

list1=[1,2,4,6,8,2,4]

result=list(set(list1))
for i in list1:
    if list1.count(i)>1:
        print(i)
