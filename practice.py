# # # n = int(input("Enter n "))
# # # result=0
# # # for i in range(0,n+1):
# # #     result=result+i
# # # print(result)
# # # n = int (input('Enter n :- '))
# # # for i in range(1,n+1):
# # #     for j in range(1,i+2):
# # #         for k in range(1,j+1):
# # #             print(k,end='')
# # #         print()
# # #     print()
# # import functools
# # names = ["wasif","ali","ahmad"]
# # l=list(map(lambda names:names.upper(),names))
# # print(l)

# # nums = [1,2,3,4]
# # print(functools.reduce(lambda x,y: x*y,nums))

# class Atm:

#   # constructor(special function)->superpower -> 
#   def __init__(self):
#     print(id(self))
#     self.pin = ''
#     self.balance = 0
#     #self.menu()

#   def menu(self):
#     user_input = input("""
#     Hi how can I help you?
#     1. Press 1 to create pin
#     2. Press 2 to change pin
#     3. Press 3 to check balance
#     4. Press 4 to withdraw
#     5. Anything else to exit
#     """)

#     if user_input == '1':
#       self.create_pin()
#     elif user_input == '2':
#       self.change_pin()
#     elif user_input == '3':
#       self.check_balance()
#     elif user_input == '4':
#       self.withdraw()
#     else:
#       exit()

# Everything in pyhton is an object .. 
# We can create our own data-types by OOP 
# Class is a blueprint , which tells us how will its object behaive 
#  [ Object is an instance of class ]

# Lets create an ATM Mechanism or Mechine 


class Atm :
    def __init__(self):
        self.pin = ''
        self.balance = 10000   # Lets set this as default .
    def menu (self):
        user_input=input(
        """
        1.Press 1 to create pin 
        2.Press 2 to change pin 
        3.Press 3 to check balance 
        4.Press 4 to withdraw
        5.Anything else to cancel 
        """
        ) 
        if user_input=='1':
            self.create_pin()
        elif user_input=='2' :
            self.change_pin()
        elif user_input=='3':
            self.check_balance()
        elif user_input=='4' :
            self.withdraw()
        else :
            print('Thanks for using this ATM')
    def create_pin(self):
        user_pin=input('Enter pin : ')
        self.pin=user_pin
        print('pin created successfully')
        self.menu()
    def change_pin(self) :
      if self.pin !='':
        old_pin=input('Enter old pin : ')
        if old_pin==self.pin:
            new_pin=input('Enter new pin : ')
            self.pin=new_pin
            print('Pin changed successfully')
            self.menu()
        else :
            print('wrong pin , try again')
            self.menu()
      else :
        print("Please create pin first")
        self.create_pin()
    def check_balance(self) :
      if self.pin !='':        
        user_pin = input ('Enter your pin : ')
        if user_pin == self.pin :
            print("Your balance is :- " , self.balance)
            self.menu()
        else :
            print("Wrong pin , try again")
            self.menu()
      else :
        print("Please create pin first")
        self.create_pin()
    def withdraw(self) :
      if self.pin !='':        
        user_pin = input("Enter your pin : ")
        if user_pin==self.pin :
            # Allow withdraw
            amount=int(input("Enter amount : "))
            if amount <= self.balance :
                self.balance=self.balance-amount
                print("withdrawal successful , please take your cash")
                print('Your balance is :- ',self.balance)
            else :
                print("Insuficient funds in your account ?")
                self.menu()
        else :
            print(" Wrong pin please try again ")
            self.menu()
      else :
        print("Please create pin first")
        self.create_pin()
      
obj=Atm()   #  Actually building the ATM  from blueprint
obj.menu()  #  Turning it on 
