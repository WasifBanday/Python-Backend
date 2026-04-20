# 1D
my_dict={'name':'Jack','age':26}

# Using []
print(my_dict['age']) # Extract age 

# Using .get
print(my_dict.get('name'))

# 2D
s={
    'name':'wasif',
    'age':'20',
    'sem':'4th',
    'subjects':{
        'maths':50,
        'dsa':67,
        'english':34
    }
}
print(s['subjects'])

# Adding key value pair 
s['gender']='male'
print(s)

s['subjects']['dsa']=75
print(s)

# Remove key value pair
# 1.pop() 
s.pop('age')
print(s)

# 2.popitem() # It deletes the last key value pair 
s.popitem()
print(s)

# 3. Del    # Deletes whole dict if no paremeter is passed (If parameter passed then it deletes that item)
del my_dict['age']
print(my_dict)

# 4.clear()    # Deletes all the items in a dictionary
my_dict.clear()
print(my_dict)



# Editing items
s['sem']='5th'
print(s)