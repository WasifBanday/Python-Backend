# Tuple in Python is similar to list , the only difference is that , we can not change elements of an tuble after decleration , where as we can change the elements of a set 
# Tuple is immutable list 
# Characteristics 
# 1.Ordered
# 2.Unchangeable 
# 3. Allow Duplicates 
# ( We will only do those things which are different in tuple from list otherwise its same as list )

# Difference between Tuple and list 
# 1.Syntax is different 
# 2.Mutability (Tuples are immutable)
# 3.Speed(Tuple are faster)
# 4.Memory ( TUples take less memory)
# 5.build in functions :- List have more buildin functions


# Creating Tuple 
# Empty Tuple 
T1=()
print(type(T1))

# Creating a tuple with a single item 
T2=(3,)  # , is important if we create a tuple with single item 
print(T2)

# Homogeneous Tuple
T3=(1,2,3,45,5,6,77,4,89,98)
print(T3)

# Hetrogeneous Tuple
T4=(1,True,'Hello')

# Tuple
T5=(1,2,3,(123,234,345))
print(T5)

# Using Type Conversion 
T6=tuple('hello')
print(T6)