def nat(n):
    if n<=0:
        return 0
    return n+nat(n-1)
print(nat(3))

def sqr(l,b):
   area = l*b
   return area
print(sqr(3,5))