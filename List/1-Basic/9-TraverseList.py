# There are two ways to traverse through a list 
# 1: indexwise  
L=[1,10,3,4]
for i in range(0,len(L)):
    print(i)    # { This prints index positions not items }
    print(L[i]) # { This prints items in that index }
    
    
# 2:  Itemwise 
L1=[1,10,3,4]
for i in L1:
    print(i)
