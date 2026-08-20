class Atm:
  __counter = 1  # Outside of all the methods, its static variable
  
  def __init__(self,name):
    self.name=name  # This is an instance variable written inside the constructor/method
    self.cid = Atm.__counter 
    Atm.__counter = Atm.__counter + 1
    
  # utility functions
  @staticmethod
  def get_counter():
    return Atm.name, Atm.__counter
c1=Atm('wasif')
c2=Atm('ankit')
print(c1.cid,c1.name)
print(c2.cid,c2.name)