class cse:
    def __init__(self,name):
        print(f"Details of {name}")
        self.t = int(input("Telugu:"))
        self.h = int(input("Hindi:"))
        self.e = int(input("English:"))
        self.m = int(input("Maths:"))
        self.s = int(input("Science:"))
    
    def total(self):
        return self.t+self.h+self.e+self.m+self.s
    
    def avg(self):
        return self.total()/5
pavan = cse("Pavan")
ram = cse("Ram")
print(pavan.total())
print(pavan.avg())

print(ram.total())
print(ram.avg())


print(ord('0'))