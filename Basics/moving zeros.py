a=[1,2,0,3,0,4,5]
for i in a:
    if i==0:
        a.remove(0)
        a.append(0)
print(a)
