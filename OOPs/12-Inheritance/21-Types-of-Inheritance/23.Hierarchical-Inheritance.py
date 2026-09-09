# Hierarchical Inheritance :- Two classes can inherit the same One class

# class 1
class phone:
    
    def __init__(self):
        print("Indide phone contructor")
            
    def buy(self):
        print("Buying a phone")
        
# class 2    
class SmartPhone(phone): # Inherits the phone class
    pass

# class 3
class FeaturePhone(phone): # Inherits the phone class
    pass

SmartPhone()
FeaturePhone()