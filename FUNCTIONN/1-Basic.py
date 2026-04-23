# Creating a function (with docstring)
def is_even(num):
    """
    Thiss functio returns if the given number is Even or Odd
    Input - Any valid int , number
    """
    if type(num) == int:
        if num % 2 ==0 :
            return 'Even'
        else :
            return 'Odd'
    else:
        return 'pagal hai kya bhosdi'
for i in range(1,11):
    x=is_even(i)
    print(x)
x=is_even('hello')
print(x)

# We can print the documentation as well 
print(is_even.__doc__)