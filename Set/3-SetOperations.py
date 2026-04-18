# There are variou methametical operations which we can do on set 
# Union(|) , intersection(&) , difference(-) , symmetric difference , membership test , iteration

# 1. Union (|)  :- It takes two sets and filter out those items which are different 
s1={1,2,3,4,5}
s2={3,4,5,6,7}
print(s1 | s2)

# 2.Intersection (&)  :- It takes two sets and filter out those items which are Common in both
print(s1 & s2) 

# 3.Difference (-)   :- It takes two sets and filter out those items which are present in the other  
print(s1 - s2) # s1 k woh items jo s2 mai present nahi hai

# 4. symmetric difference (^) :- It takes two sets and filter out those items which are not common  
print(s1 ^ s2)

# 5. Membership test (in , not in )
print(1 in s1)
print(1 not in s1)

# 6. Iteration 
for i in s1 :
    print(i)