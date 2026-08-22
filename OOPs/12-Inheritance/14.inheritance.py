# Constructor Example : 2  ( child with constructor )
# * when child have a constructor then parents constructor not gets called * 

class Phone:
    def __init__(self,price,brand,camera):
        print('Inside phone constructor')
        self.price=price
        self.brand=brand
        self.camera=camera
    def buy(self):
        print("Buying phone")

class SmartPhone(Phone):  # child with constructor
    def __init__(self, os, ram):
        self.os=os
        self.ram=ram
        print('inside SmartPhone constructor')
        
s=SmartPhone('apple',15)
# s.brand  #Through error