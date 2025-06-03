a=[1,3,2,-5,-4]
pos=0
neg=0
for i in a:
    if i>0:
        pos+=i
    else:
        neg+=i
print([pos,-neg])
