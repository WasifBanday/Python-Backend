# Reference Variables
#   Reference variables hold the objects
#   We can create objects without reference variable as well, but then won't be able to access it.
#   An object can have multiple reference variables
#   Assigning a new reference variable to an existing object does not create a new object

class person :
    def __init__(self):
        self.name='wasif'
        self.gender='male'
        
print(person()) # object created without referance 
p=person() # object created with referance 
print(p)
a=p # another object pointing to same referance
print(a)