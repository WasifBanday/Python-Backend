# Multiple Inheritance :- One class can access properties of two parents 

class phone:
    
    def __init__(self):
        print("inside phone constructor")      
    def buy(self):
        print("buying a phone")

class product:
    def review(self):
        print("Customer review")

class smartphone(phone,product): # inherits Both classes
    pass

s=smartphone()
s.buy()
s.review()