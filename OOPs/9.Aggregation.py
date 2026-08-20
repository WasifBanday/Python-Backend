# Aggregation :- It's actually a class relationship type [like, inheritance]
# Aggregation it has this relationship : [has a]  relation
# Aggregation : One class owns the other class 
# example :- customer has a address {here : 'has a' is relation} 

# Now code example :
class customer :
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address
        
    def print_adddress(self):
        print(self.address.city,self.address.pin,self.address.state)
        
class address :
    def __init__(self,city,pin,state):
        self.city=city
        self.pin=pin
        self.state=state
        
add1=address('srinagar',193001,'kashmir')
cust=customer('wasif','male',add1)
cust.print_adddress()