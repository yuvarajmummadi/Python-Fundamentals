def fibon(n):
    if n<=1: return n
    else:
        return fibon(n-1)+fibon(n-2)
print(fibon(5))
n = 23
sum = 0
if n<=0:
    print("Enter a positive number")
else:
    print("Fibo series")
    for i in range(n):
        sum+= n
        print(fibon(i))
    print(sum)