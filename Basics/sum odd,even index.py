a=[1,2,3,4,5,6]
odd_sum=0
even_sum=0
for i in range(len(a)):
    if a[i]%2==0:
        even_sum+=a[i]
    else:
        odd_sum+=a[i]
print(even_sum)
print(odd_sum)
if even_sum>odd_sum:
    print("even")
else:
    print("Odd")
