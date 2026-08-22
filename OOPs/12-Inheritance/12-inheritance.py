# One class {child class} can resue the data and behavior of other class {parent class} instead of writing everything again 

# parent class
class User:
    def __init__(self):
        self.name='wasif'
        self.gender='male'
    def login(self):
        print('login')

# child class
class Student(User):
    def enroll(self):
        print('Enroll successfully')

u=User()
s=Student()
print(s.name)
s.login()
s.enroll()