# Accessing item ( Doesn't work because its unordered)
# Edit items (Same we can't)

# Adding items Using { Add() and update() }
 # Add()
s1={1,2,3,4}
s1.add(5)
print(s1)

 # update()
s1.update([6,7,8,9])
print(s1)

# Deleting items { del() , discard() , remove() , pop() , clear() }
# del()
s2={1,2,3,4,5,6}
print(s2)
del s2
# print(s2) # Whole set will be deleted

# discard()   :- deletes the value given in braces   (Doesn't through error if the given item is not available)
s3={1,2,3,4,5,6}
s3.discard(4)
s3.discard(40)  # Item not available but still no error
print(s3)

# remove()   :- Same as discard , but it will through an error if  item is not available in a set
s3.remove(6)
# s3.remove(30)  # It will through error 
print(s3)

# pop()    :- Deletes any item randomly 
s3.pop()
print(s3)
# clear()  :- Clears/deletes all items in a set 
s3.clear()
print(s3)