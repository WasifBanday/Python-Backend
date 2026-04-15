# List comprhension provide us a concise way of creating list 

# newlist=[expression for item in iterable if condition == True]

# Problem 1 
# Add 1 to 10 numbers to a list 
L=[i for i in range(1,11)]
print(L)

# problem 2 
# Scalar multiplecation on a vector 
v=[2,3,4]
s=-3
print([s*i for i in v])

# Problem 3 
# Add squares 
L1=[1,2,3,4,5]
print([i**2 for i in L1])

# Problem 4 
# Print all the numbers which are divisible by 5 b/w 1 to 50 
numbers=[i for i in range(1,51) if i%5==0]
print(numbers)

# Problem 5 
# Find languages which starts with letter 'P'
Languages=['Java','GoLang','Python','Php','Cpp','JavaScript']
LanP=[i for i in Languages if i.startswith('P')]
print(LanP)

# Problem 6 
# Nested if with list comprehension

basket=['apple','mango','grapes','orange']
my_fruits=['apple','gauva','peach','mango']
# Add new list from my_fruits and items if the fruit exist in basket and also starts with letter 'a'
print([i for i in my_fruits if i in basket if i.startswith('a')])

# Problem 7 
# cartesian Prouct 
l1=[1,2,3,4]
l2=[5,6,7,8]
print([i * j for i in l1 for j in l2])