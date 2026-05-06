# Map --> Take two inputs [1st ->function .  2nd ->iterable]
#   map(function,iterable)

# Example 1 : Square the item of a list 
print(list(map(lambda x:x**2 , [1,2,3,4,5])))

# Example 2 : Odd / Even 
l=[1,2,3,4,5,6,7]
print(list(map(lambda x:'even' if x % 2==0 else 'odd' , l)))