# 1:- Arithematic [ + , * ]
L1=[1,2,3]
L2=[4,5,6]
# Concatenation/Merging
print(L1+L2)
print(L1*3)

# 2:- Membership [ in , not in ]
L3=[1,2,3,4,5]
print(5 in L3)
print(5 not in L3)

L4=[1,2,3,4,[5,6]]
print(5 in L4) # false , because 5 is in a list which as whole list is present in L4 
print([5,6] in L4) # True its as list
