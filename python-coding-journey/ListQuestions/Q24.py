# 24. Find missing number in array

numbers = list(map(int,(input("Enter numbers: ").split())))

expectedNumber=((len(numbers)+1)*((len(numbers)+1)+1))//2
actualNumber=0
for num in numbers:
    actualNumber+=num

print("Missing number: ", expectedNumber-actualNumber)
    