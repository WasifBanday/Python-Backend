# Set Characterstics
# 1. Mutable
# 2. Unordered
# 3. No duplicates
# 4. Can't contain mutable data types 

# Creating set 

# empty
s={}  # This is not a set because set and dictionery share the same syntax while creating , The default behavior is dict 
s=set() # this is an empty set

# 1D
s1={1,2,3}
print(s1)

# 2D
# s2={1,2,3,{1,2,3}}   # Not allowed because set can't contain mutable items 

# Hetrogeneous set
s2={1,'hello',4.5,True}   # True : didn't got printed because of 1 , duplicates are not allowed 
print(s2)

# using type conversion 
s3=set([1,2,3])
print(s3)

# duplicates not allowed 
s4={1,1,2,2,2,2,2,3,4,4,4,4,5,5,5,5,5}
print(s4)

# Unordered
s5={1,2,3}
s6={3,2,1}
print(s5==s6)