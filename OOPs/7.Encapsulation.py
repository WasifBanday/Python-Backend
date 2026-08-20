# Firstly there is nothing truely private in python 
# Encapsulation : Bundling data and the methods that operate on in inside a class, while controlling how that data can be accessed or modified 
# * Keep the data inside the class and control access to it throuh methods like getter and setter *

class person :
    def __init__(self,age):
        self.age=age
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age>=0:
            self.__age=age
            print('Age updated successfully, you are now {} years old'.format(self.__age))
        else:
            print("Age cannnot be negative")
p=person(20)
p.set_age(2)