# 1- isalnum()  :- Checks if the string has only Alphabets and numbers 
print('wasif123'.isalnum())
print('waif12%'.isalnum())

# 2- isalpha() :- Checks if the string has only alphabets or not
print('wasif'.isalpha())
print('wasif12'.isalpha())

# 3- idigit() :- Checks if the strings has only digits or not 
print('1234'.isdigit())
print('123wasif'.isdigit())

# 4- isidentifiers() :- validate string as legal Python identifier
#                       A valid identifier:
#                       Contains only letters (a-z, A-Z), digits (0-9), or underscores _
#                       Does not start with a digit
#                       Is not empty                      

print('wasif121'.isidentifier())
print('121wasif'.isidentifier())