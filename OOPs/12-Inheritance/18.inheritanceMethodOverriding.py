# Method overriding 
# If parent and child class have same name of attribute or method, then childs attribute or method will be executed 

class phone :
    
    def __init__(self):
        print("inside phone constructor") # This will work
        
    def buy(self):
        print("Buying a phone") # This won't work
    
class SmartPhone(phone):
    
    def buy(self):
        print("Buying SmartPhone") # This will work

s=SmartPhone()
s.buy()