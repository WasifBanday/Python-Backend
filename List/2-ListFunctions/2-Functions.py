# count : It tells us how many times some item has been repeated in a list
L1=[1,2,3,4,5,4,32,7,8,9,8,43,2,4,5,65,4,4]
print(L1.count(4))

# Index : Tells index number of a perticular item
print(L1.index(32))

# reverse : It permanently reverses the list ... 
L2=[1,2,3,4,5]
L2.reverse()
print(L2)

# sort (not sorted)  :- It also permanently sorts the list , but sorted doesn't permanently sorts the list
L3=[1,2,3,4,5,4,8,43,2,4,5]
print(sorted(L3))
print(L3)

L3.sort()
print(L3)

# copy : creates copy of list in the memory 
L4=[1,2,4,6,8,3,4]
print(L4)
print(id(L4))
L5=L4.copy()
print(L5)
print(id(L5))