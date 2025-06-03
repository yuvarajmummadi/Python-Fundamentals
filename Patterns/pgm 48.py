# Pattern 7
n = 5
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)  #Pyramid
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i) #Reverse Pyramid

# Output:
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     *