#method-1
a=[1,0,2,3,3,4,5,10]
print(set(a))
#method-2
a=[1,0,2,3,3,4,5,10]
res=[] #to create empty list
for i in a:
    if i not in res:
        res.append(i)
print(res)
