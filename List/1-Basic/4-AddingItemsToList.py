# There are three functions which help us to add items in a list , that are :-  .append() , .extend() and .insert() 

# 1:- .append()  {Adds item to a list at its end , and it adds only one item at a time}
L1=[1,2,3,4,5,6]
L1.append(7)
print(L1)

# 2:- .extend() {Adds multiple items to a list in one go}
L2=[1,2,3,4]
L2.extend([5,6,7,8])
print(L2)

# 3:- .insert() {Adds one item to a list at desired position , where ever you want}
L3=[1,2,3,4,5,6,7,8,9,10]
# will add 100 at index 1 
L3.insert(1,100)
print(L3)