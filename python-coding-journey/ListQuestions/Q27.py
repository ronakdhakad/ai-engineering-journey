# 27. Move all zeros to end

numbers = list(map(int,(input("Enter numbers: ").split())))

for num in range(len(numbers)-1,-1,-1):
    if(numbers[num]==0):
        numbers.pop(num)
        numbers.append(0)
print(numbers)