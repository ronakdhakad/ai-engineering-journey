# 5. Check if a year is a leap year
a=int(input("Enter a year: "))

if((a%4==0 and a%100!=0) or (a%400==0)):
    print(a, " is leap year")
else:
    print(a, " is not a leap year")
