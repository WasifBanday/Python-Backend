# BASIC FUNCTIONS :- len / max / min / sorted

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

# 1 .len()  # Gives no. of keys
print(len(s))

# 2 .sorted()  # Sort keys (Accending order)
print(sorted(s))

# 3 .max()    # Maximum based on ASCII value
print(max(s))
# 4 .min()    # Minimum based on ASCII value
print(min(s))



# OTHER FUNCTIONS :- .items() / .keys() / .values()

# 1.items()     # Converts dict into tuples in order of keys and values 
print(s.items())

# 2.keys()      # prints all the keys in one go 
print(s.keys())

# 3.values()    # Print all the values in one go 
print(s.values())

# 4x.update()   # it updates one dictionaries from another 
d1={1:2,3:4,4:5}
d2={5:6,7:8}
d1.update(d2)
print(d1)
