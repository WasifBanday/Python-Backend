# Now we can use both the constructors i,e in parent and in child as well 
class Parent :
    
    def __init__(self,price,brand,camera):
        print("Inside parent constructor")
        self.price=price
        self.brand=brand
        self.camera=camera
        
class SmartPhone(Parent):
    
    def __init__(self, price, brand, camera,os,ram):
        
        super().__init__(price, brand, camera) # calling parent constructor
        self.os=os
        self.ram=ram
        print("Inside SmartPhone Constructor")

s=SmartPhone(20000,"samsung",12,"Andriod",2)
print(s.os)
print(s.ram)