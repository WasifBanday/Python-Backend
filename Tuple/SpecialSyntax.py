# Tuple unpacking 
a,b,c = (1,2,3)
print(a,b,c) # a=2  b=2  c=3

# Problem :- Swap Values
a=1 
b=2 
a,b = b,a
print(a,b)

# Others 
a,b,*others=(5,2,3,44,5,6,1,2,2,3,4,5,5,6,7)
print(a,b)

print(others)