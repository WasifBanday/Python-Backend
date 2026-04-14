# Accessing items from a list 

# 1D
# 1--> Positive Indexing 
L1=[1,2,3,4,5,6]
print(L1[0])

# 2--> Negative Indexing
L2=[2,3,4,5,6,7]
print(L2[-1])


# 2D
L2=[1,2,3,[1,10,3]]
print(L2[3][1])  # 10 , will be printed because its in the 4th item of a list which itself is a list in a list

# 3D
L3=[[[1,2],[3,4]],[[5,6],[7,8]]]
# print 7 
print(L3[1][1][0])

