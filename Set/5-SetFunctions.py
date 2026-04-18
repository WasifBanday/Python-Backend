# there are some other function of set 
# [ isdisjoint , issubset , issuperset ] :- these give us true,false 

# 1.isdisjoint() :- Returns True if two sets have NO common elements
s1={1,2,3,4}
s2={5,6,7,8}
print(s1.isdisjoint(s2))

# 2.issubset() :- Returns True if all elements of one set are present in another set 
s1={1,2,3,4}
s2={2,3}
print(s2.issubset(s1))

# 3.issuperset() :-Returns True if a set contains all elements of another set {issubset ka ulta}
s1={1,2,3,4}
s2={2,3}
print(s2.issuperset(s1))
print(s1.issuperset(s2))

# 4.copy()  :- Creates shallow copy 
s3={5,6,7,8}
s4=s3.copy()
print(s3)
print(s4)