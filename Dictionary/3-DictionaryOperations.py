# 1: Membership   ( Gives output based on key not value )
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
print('name' in s)

# 2: Iteration 
for i in s :
    print(i) # This will only print the keys 
for i in s:
    print(i,s[i])  # This will print both keys and values 