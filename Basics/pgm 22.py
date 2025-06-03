class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_infor(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Year : {self.year}")
        
car1 = Car("XUV",400,2025)
car1.display_infor()