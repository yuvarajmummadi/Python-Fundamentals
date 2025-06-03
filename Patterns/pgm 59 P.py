n = 5
for i in range(n):
    for j in range(i+1):
        print(chr(ord("a")+i),end = " ")
    print()
# Output:
# a 
# b b 
# c c c 
# d d d d 
# e e e e e