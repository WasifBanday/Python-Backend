# Login program and identation 
# email -> wasifahmad@gmail.com
# password -> '1234'

email=input('Enter email : ')
password=input('Password : ')
if email== 'wasifahmad@gmail.com' and password=='1234':
    print('Welcome') 
elif email=='wasifahmad@gmail.com' and password !='1234':
    print('incorrect password')
    password=input('Enter password again : ')
    if password=='1234':
        print('ohooo , Welcome ')
    else:
        print('Nahi bhai , Password ptah krke ahh')
else:
    print('Incorrect email and password')