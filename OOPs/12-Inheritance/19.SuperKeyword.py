# By using "Super" keyword we can access method/instance variables from parent class 
# Super Keyword is always used inside child class 
# we can not use super keyword outside class 
# super() is used to access/call parent-class methods, not the parent's instance variables(variable inside def() ). 

class Parent :
    
    def __init__(self,price,brand,camera):
        print("Inside parent class")
        self.price=price
        self.brand=brand
        self.camera=camera
    
    def buy(self):
        print("Buying a phone")

class SmartPhone(Parent):
    
    def buy(self):
        print("Inside child class")
        # Syntax to call parent ka "Buy" method from child
        super().buy()

s=SmartPhone(200000,"Apple","13px")
s.buy()