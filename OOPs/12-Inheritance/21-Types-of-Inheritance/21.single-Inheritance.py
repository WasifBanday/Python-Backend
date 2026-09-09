# Single Inheritance :- child can access the property of father only 
class phone :
    
    def __init__(self,price,brand):
        print("inside phone constructor")
        self.price=price
        self.brand=brand
    
    def buy (self):
        print("Buying phone")

class smartphone(phone):
    pass
smartphone(1000,"Apple")