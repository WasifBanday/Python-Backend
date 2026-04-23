# What will happen without return statement 
# If we write code without a return statement , it will still return a value 'none'

def check (num):
    if num % 2 == 0 :
        print('Even')
    else:
        print('Odd')
print(check(7))  # No return statement it will print 'none' as default return