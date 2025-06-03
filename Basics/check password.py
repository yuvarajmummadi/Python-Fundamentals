def verification(a):
    alp=dig=sym=up=lo=False
    if not (8<=len(a)<=10):
        return False
    for i in a:
        if i.isalpha():
            if i.isupper():
                up=True
            else:
                lo=True 
        if i.isdigit():
            dig=True
        if i in "@_":
            sym=True
    if sym and dig and up and lo:
        return True
    return False           
a=input()
print(verification(a))
