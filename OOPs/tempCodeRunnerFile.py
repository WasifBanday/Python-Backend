# Pass by Reference 
class Person :
    def __init__(self, name):
        self.name=name
# outside the class --> so its function , not method
def greet(Person):
    p=Person.name='Ankit'
    print(Person.name)
p=Person('wasif')
x=greet(p)
print(p.name)
print(x.name)