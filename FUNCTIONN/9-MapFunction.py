# Map --> Take two inputs [1st ->function .  2nd ->iterable]
#   map(function,iterable)

# Example 1 : Square the item of a list 
print(list(map(lambda x:x**2 , [1,2,3,4,5])))

# Example 2 : Odd / Even 
l=[1,2,3,4,5,6,7]
print(list(map(lambda x:'even' if x % 2==0 else 'odd' , l)))

# Example 3 : Fetch names from a list of dict
users=[
    {
        'name' : 'Rahul',
        'age': 20,
        'gender':'male'
    },
    {
        'name' : 'wasif',
        'age': 21,
        'gender':'male'
    },
    {
        'name' : 'Aisha',
        'age': 19,
        'gender':'female'
    }
]
print(list(map(lambda users:users['gender'],users)))