def fun(n):
    k = 0
    while k<n:
        yield k
        k+=1
print(list(fun(7)))#generator function
