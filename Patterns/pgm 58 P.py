n = 5
for i in range(1,n+1):
    for j in range(0,i):
        print(chr(ord("a")+j),end = " ")
    print()

# Output:
# a 
# a b 
# a b c 
# a b c d 
# a b c d e