# Since we can not access attribute of other class which are private, so for that we use 'setter' method 
class customer :
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address
        
    def print_adddress(self):
        print(self.address.get_city(),self.address.pin,self.address.state)
        
class address :
    def __init__(self,city,pin,state):        
        self.__city=city
        self.pin=pin
        self.state=state
    def get_city(self): # get : used for getting private attribute
        return self.__city
add1=address('srinagar',193001,'kashmir')
cust=customer('wasif','male',add1)
cust.print_adddress()