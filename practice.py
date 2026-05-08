# # n = int(input("Enter n "))
# # result=0
# # for i in range(0,n+1):
# #     result=result+i
# # print(result)
# # n = int (input('Enter n :- '))
# # for i in range(1,n+1):
# #     for j in range(1,i+2):
# #         for k in range(1,j+1):
# #             print(k,end='')
# #         print()
# #     print()
# import functools
# names = ["wasif","ali","ahmad"]
# l=list(map(lambda names:names.upper(),names))
# print(l)

# nums = [1,2,3,4]
# print(functools.reduce(lambda x,y: x*y,nums))

class Atm:

  # constructor(special function)->superpower -> 
  def __init__(self):
    print(id(self))
    self.pin = ''
    self.balance = 0
    #self.menu()

  def menu(self):
    user_input = input("""
    Hi how can I help you?
    1. Press 1 to create pin
    2. Press 2 to change pin
    3. Press 3 to check balance
    4. Press 4 to withdraw
    5. Anything else to exit
    """)

    if user_input == '1':
      self.create_pin()
    elif user_input == '2':
      self.change_pin()
    elif user_input == '3':
      self.check_balance()
    elif user_input == '4':
      self.withdraw()
    else:
      exit()