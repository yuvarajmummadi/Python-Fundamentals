string = "ram"
for i in range(1,len(string)+1):
    print(string[:i])
for i in range(len(string)-1,0,-1):
    print(string[:i])
    
# Output:
# r
# ra
# ram
# ra
# r