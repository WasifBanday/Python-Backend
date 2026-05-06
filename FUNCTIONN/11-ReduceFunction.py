# Reduce function ( import module to use it )
# It works on 2 items at a time 
import functools

# Example - Sum of all items 
print(functools.reduce(lambda x,y : x+y , [1,2,3,4,5,6]))

# Example - find minimum of all items 
print(functools.reduce(lambda x,y:x if x<y else y , [23,11,34,56] ))