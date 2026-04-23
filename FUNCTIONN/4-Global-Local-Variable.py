#  Global and Local Variable 
#   1
def f(y):
    x=1 # This 'x' is local variable 
    x=x+1
    print(x)
x=5 # This 'x' is global variable
f(x)
print(x)


#   2
def g():
    # a=2
    print(x) # Local can access global variable
    # x=x+1 # This is not allowed because we can use global variable but can't change it 
    print(x+1)
x=5
g()
print(x)
# print(a) # Global can't access Local variable 


#   3 :- we can change global variable from local varialble using [ 'global' keyword ]
def y(g):
    global a  # This changes global variable as well
    a=a+1
    print(a)
a=2
y(g)