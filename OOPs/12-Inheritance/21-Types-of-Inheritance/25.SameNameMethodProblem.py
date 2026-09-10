class phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.price=price
        self.brand=brand
        self.camera=camera
    def buy(self):
        print("Buying a phone")

class product:
    def buy(self):
        print("Buying a product")

# Method Resolution Order (which comes 1st in order)
class smartphone(product,phone): # Here on calling the ' s.buy() '  products buy() will be called because its 1st in receiving
    pass
s=smartphone(2000,"apple","12px")
s.buy()