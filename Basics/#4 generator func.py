#4 generator func
def fun(n):
    i=0
    while i<n:
        yield i
        i+=1
print(list(fun(5)))