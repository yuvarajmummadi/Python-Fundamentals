def minll(n,i=0):
    if i==len(n)-1:
        return n[i]
    return min(n[i],minll(n,i+1))
n=[3,5,2,6,0,-1]
print(minll(n))

def maxl(n,i=0):
    if i == len(n)-1:
        return n[i]
    max = maxl(n,i+1)
    return n[i] if n[i]>max else max
n = [1000,2787,4,5,100]
print(maxl(n))