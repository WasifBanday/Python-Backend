# Zip() :- Basically helps us to add two lists and form 3rd new List from it 
L1=[1,2,3,4]
L2=[-1,-2,-3,-4]
 # Now items of the list L1 and L2 will get add , index by index 
print(list(zip(L1,L2)))
print([i+j for i,j in zip(L1,L2)])