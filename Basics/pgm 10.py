#minimum in a given list
#normal function
def minl(n):
    min = n[0]
    for i in range(1,len(n)):
        if n[i]<min:
           min = n[i]
    return min
n=[3,5,2,6,0,-1]
print(minl(n))