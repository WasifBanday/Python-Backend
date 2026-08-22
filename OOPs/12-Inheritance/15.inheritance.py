# Child cannot access private members of the class 

class Phone:
    def __init__(self,price,brand,camera):
        print('Inside phone constructor')
        self.__price=price
        self.brand=brand
        self.camera=camera
    def __show(self):
        print(self.__price)

class SmartPhone(Phone):  # child with constructor
    def check(self):
        print(self.__price)    
s=SmartPhone(20000,'apple',15)
print(s.brand)
s.__show()  # This member won't get printed because it's private ...
# print(s.__price)  # This attribute won't get printed because it's private ... 