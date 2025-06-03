#         
def sod(n):
    sum = 0
    if n<10: return n
    return sod(n%10)+sod(n//10)
print(sod(1235455478))
