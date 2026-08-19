# Pass by Reference 
class Person :
    def __init__(self, name,gender):
        self.name=name
        self.gender=gender
# outside the class --> so its function , not method
def greet(person):
    print("Hi my name is",person.name,"and i am a",person.gender)
    p1=Person('Ankit','male')
    return p1
p=Person('wasif','male')
x=greet(p)
print(x.name)
print(x.gender)