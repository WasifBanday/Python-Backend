# Lets create owr own datatype , Fraction 

class Fraction :
    
    # Parameterized constructor : Expects some inputs 
    def __init__(self,x,y):
        self.num=x
        self.den=y
    
    def __str__(self):    # this determines how object looks
        return '{}/{}'.format(self.num , self.den)
    
    def __add__(self, other):
        new_num=self.num  * other.den + self.den * other.num 
        new_den=self.den * other.den 
        return '{}/{}'.format(new_num , new_den)
    
    def __sub__(self, other):
        new_num=self.num  * other.den - self.den * other.num 
        new_den=self.den * other.den 
        return '{}/{}'.format(new_num , new_den)
    
    def __mul__(self, other):
        new_num=self.num  * other.num 
        new_den=self.den * other.den 
        return '{}/{}'.format(new_num , new_den)
    
    def __truediv__(self, other):
        new_num=self.num  * other.den 
        new_den=self.den * other.num 
        return '{}/{}'.format(new_num , new_den)

    def convert_to_decimal(self):
        return self.num / self.den
    
fr1=Fraction(2,4)
print(fr1)
fr2=Fraction(5,4)
print(fr2)

print(fr1.convert_to_decimal())

print(fr1 + fr2)
print(fr1 - fr2)
print(fr1 * fr2)
print(fr1 / fr2)