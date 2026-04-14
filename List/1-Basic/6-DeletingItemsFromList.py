# DELETING
# 1-> Using del :- It basically deletes the whole lists(reference) or list items as well by indexing and slicing if the parameters are passed
L1=[1,2,3,4]
del L1
# print(L1)   # Will show not defined 

# 2-> .remove()  { Can delete items by value as well }
L2=[1,2,3,4]
L2.remove(3)
print(L2)

# 3-> .pop()  { delete items by index values , default index is : -1}
L3=[1,2,3,4,5,6,7,8]
L3.pop()   # will delete item which is at last , because no index no is being passed
print(L3)

L3.pop(3)   # will delete item which is at index 3
print(L3)

# 4-> .clear()  { deletes all the items in a list}
L4=[2,34,6,9,8,4,86,5,44]
L4.clear()
print(L4)