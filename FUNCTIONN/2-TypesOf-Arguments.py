# Types Of Arguments 

# 1 :- Default Arguments [ Setting default values in a parament] [ Used to prevent from an error , If you pas less arguemnts or no agrument ]
def power(a=1,b=2):
    return a**b
print(power())
print(power(2))
print(power(2,3))

# 2 :- Positional Argument [Jis order mai aap arguments ko bejoge usi order mai parameter unko receive krega]
# example
print(power(4,5)) # a=4 and b=5 [simple default behaviour]

# 3 :- Keyword Argument [ Passing argument direct to parameter names]
print(power(b=3,a=2))

#   *args and **kwargs :- Special python keyword that are used to pass the variable length of arguments to a function
#     Order of arguments matter ( Normal -> *args -> **kwargs )
#     The word '*args' and '**kwargs' are only a convention , we can use any name of our choice

# *args [  Allows us to pass a variable number of non-keyword arguments to a function ]

def multiply (*args):
    product=1
    for i in args:
        product=product * i
    print(args)
    return product     
result = multiply(10, 11)
print(result)


# **kwargs [ Allows us to pass any number of keyword arguments ]
            # keyword argument means that they contain a key , value pair , like python dictionary 
            
def display(**kwargs):
    for (key,value) in kwargs.items():
        print(key , ' --> ' , value)
display(india='delhi' , srilanka='colombo')