a=[1,3,2,5,3,2,2]
res={} #to create empty dictionary
for i in a:
    if i in res:
        res[i]+=1
    else:
        res[i]=1
print(res)
