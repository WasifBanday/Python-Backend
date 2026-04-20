# Dictionary in pyhton is a collections of key , values 
# Characterstics of dict
#   1. mutable 
#   2. indexing have no meaning 
#   3. keys cant be duplicated 
#   4. keys cant be mutable items


# create 
# Empty
d={}

# 1D 
d1={'name':'wasif' , 'age':20 , 'gender' :'male'}


# 2D 
s={
    'name':'wasif',
    'age':'20',
    'sem':'4',
    'subjects':{
        'maths':50,
        'sciene':67,
        'english':34
    }
}
print(s)

# Using sequence and dict function
d2=dict([('name','wasif'),('age',32)])
print(d2)

# Duplicate keys
d3={'name':'wasif','name':'aisha'}  # pehla wala replace hota hai agar same key ho toh 
print(d3)