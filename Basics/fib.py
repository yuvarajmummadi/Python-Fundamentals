n=6
if n<=1:
    print(n)
else:
    first=0
    second=1
    for i in range(n-1):
        third=first+second
        first=second
        second=third
print(third)
