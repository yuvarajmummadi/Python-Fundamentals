n=5
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
print("prime" if count==2 else "not a prime")
#method-2
n=15
count=0
for i in range(2,n):
    if n%i==0:
        print("not a prime")
        break
else:
    print("prime")
#method-3
n=6
count=0
for i in range(2,n//2):
    if n%i==0:
        print("not a prime")
        break
else:
    print("prime")
#method-4
n=6
count=0
for i in range(2,(n//2)+1):
    if n%i==0:
        print("not a prime")
        break
else:
    print("prime")
