n=123
#123%10=3(res)
#123//10=12
#3*10=30+12%10=32
#32*10=320+1=321
n=12121
res=0
temp=n
while n:
    rem=n%10
    res=(res*10)+rem
    n//=10
print("palindrome" if res==temp else "not palindrome")
