# Frozenset :- Its an immutable version of python set  , Once created, you cannot add, remove, or change elements
 # Create 
fs=frozenset([1,2,3,4])
print(fs)

#  IN this frozen set :- All read functions will work like (.difference() , .union() , .intersection() , .isdisjoint())
                        # But write operation will not work like ( fs.add()  , fs.remove() , fs.discard() , fs.pop() , fs.clear()           

# 2D frozenset 
fs1=frozenset([1,2,3,frozenset([4,5])])
print(fs1)


# Set comprehension :- 
comp={i for i in range(1,11) if i>5}
print(comp)