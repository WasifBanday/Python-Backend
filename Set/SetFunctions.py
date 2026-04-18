# 1.common functions [len() , max() , min() , sorted() , sum()] --> Same as other

s1={1,2,3,4,5}
s2={3,4,5,6,7} 
print(sum(s1)) # if we try to sum(s1 + s2) it will give an error , because sets don’t support + 

# Other functions [Union/update :- ]
# 1.union :- same as union(|)
print(s1.union(s2))
print(sum(s1 | s2))  # It adds the items of both the sets which are different in both sets

# 2.update() :- [pehle wle mai permanent change ahjata hai]
s1.update(s2)  # Take all elements from s2 and add them into s1 [ It modifies s1 in-place (no new set is created) ]
print(s1)

# 3.intersection_update()  :- Keeps only common elements in s3
s3={1,2,3,4,5}
s4={3,4,5,6,7} 
s3.intersection_update(s4)
print(s3)

# 4. difference_update() :- Remove elements from s5 that are present in s6
s5={1,2,3,4,5}
s6={3,4,5,6,7} 
s5.difference_update(s6)
print(s5)

# 5. symmetric_difference_update() :- Keeps elements that are NOT common in both
s7={1,2,3,4,5}
s8={3,4,5,6,7} 
s7.symmetric_difference_update(s8)
print(s7)