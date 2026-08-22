# What gets inherited are [ constructor,Non-private attribute and Non-private method ]

# Constructor Example : 1  ( child without constructor )
class Phone:
    def __init__(self,price,brand,camera):
        print('Inside phone constructor')
        self.price=price
        self.brand=brand
        self.camera=camera
    def buy(self):
        print("Buying phone")

class SmartPhone(Phone):  # child without constructor
    pass
s=SmartPhone(20000,'apple',15)
s.buy()