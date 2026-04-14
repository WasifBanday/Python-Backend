# since list is flexible/mutable/changeable we can edit or delete items from it ... 
# EDITING
# 1-> Editing [By Indexing]
L1=[1,2,3,4,5,6]
# change 5 to 500 in L1 list 
L1[4]=500
print(L1)

# 2-> Editing [By Slicing]
L2=[1,2,3,4,5,6]
# change 2,3,4 to 200,300,400 in L2 list 
L2[1:4]=[200,300,400]
print(L2)