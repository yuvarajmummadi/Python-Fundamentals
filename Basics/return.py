even=[]
odd=[]
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
for i in range(len(even)):
    for j in range(len(even)-1):
                if even[j]>even[j+1]:
                    even[j],even[j+1]=even[j+1],even[j]
result=even+odd
print(result)
