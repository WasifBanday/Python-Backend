# Multi-Level-inheritance :- here child can access from its father and grand father and grand grand father and so on 
class Product:
    
    def review(self):
        print ("Product customer review")

class Phone(Product): # inherits product class
    
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone): # inherits phone class 
    pass

s=SmartPhone(20000, "Apple", 12)

s.buy()
s.review()