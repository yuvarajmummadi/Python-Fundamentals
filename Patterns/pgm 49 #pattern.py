#pattern 7
n = 5
for i in range(1,n+1):
    print("* "*n)  #rect


n = 5
for i in range(1,n+1):
    if i==1 or i==n:
        print("* "*n)
    else:
        print("* "+"  "*(n-2)+"*")
# Output:
# * * * * * 
# *        *
# *        *
# *        *
# * * * * *