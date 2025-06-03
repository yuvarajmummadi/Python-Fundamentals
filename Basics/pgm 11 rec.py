# #using recursion
def minll(n,i=0):
    if i==len(n)-1:
        return n[i]
    min = minll(n,i+1)
    return n[i] if n[i]<min else min
n=[3,5,2,6,0,-1]
print(minll(n))