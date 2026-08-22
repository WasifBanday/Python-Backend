class parent :
    
    def __init__(self,num):
        self.num=num
    
    def get_num(self):
        return self.num

class Child(parent):
    
    def __init__(self,val, num):
        self.__val=val
        
    def get_val(self):
        return self.__val

son=Child(100,10)
print("child: Val: ", son.get_val())    # Will be printed
print("Parent: Num: ", son.get_num())   # Will not work