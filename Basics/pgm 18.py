year = int(input())
leap = False
if year%400==0:
    leap = True
elif year%100==0:
    leap = False
elif year%4==0:
    leap = True
print("leap year" if leap else "Not a leap")
