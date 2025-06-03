class house:
    def hall(self,l,b):
        return 2*l*b
    def bed_room(self,l,b):
        return l*b
    def kitchen(self,s):
        return s*s
person = house()
print(person.hall(4,5))
print(person.bed_room(5,6))
print(person.kitchen(5))

class pavan:
    def bike(self):
        print("Pavan")
    
class vij:
    def bike(self):
        print("vIJAY")
    
class pradeep(pavan,vij):
    def __init__(self):
        super().__init__()
        print("No")                                                                                                                                                                                                               
obj = pradeep()