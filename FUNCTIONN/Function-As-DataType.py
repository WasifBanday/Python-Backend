# Function in python is a data type (like :- other data types int,list,set,dictionery etc)

# Type and id 
def square (num):
    return num**2
print(type(square))
print(id(square))

# reassign 
x=square
print(id(x))  # this will have same id as [ print(id(square)) ]

# deleting a function
# del square

# storing function in a variable 
L=[1,2,3,4,square]
print(L)

# {Function is an immutable data-type} #


# Returning a function 
def f():
    def x(a,b):
        return a+b
    return x
val=f()(3,4)
print(val)

# Function as argument 
def func_a():
    print('inside func_a')
def func_b(z):
    print('inside func_b')
    return z()
print(func_b(func_a))

# Benefits of using a function 
#   1- Code Modularity
#   2- Code Readibality
#   3- Code Reusability