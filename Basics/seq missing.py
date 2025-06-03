a=[1,2,3,4,5]
b=[1,2,4,5]
for i in range(len(b)):
    if a[i]!=b[i]:
        print(i)
        break
else:
    print(i+1)   
