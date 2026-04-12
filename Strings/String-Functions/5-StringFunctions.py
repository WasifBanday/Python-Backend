# 1- Split()  :- Breaks String where spaces found by default , but is something passed in Split() , then it will break it there 
print('hey my name is wasif i am from kupwara'.split())
print('hey my name is wasif and i am from kupwara'.split('and'))

# 2- Join()  :- Reverse of split , joins the list as string
print(' '.join(['hey', 'my', 'name', 'is', 'wasif','and' , 'i', 'am', 'from', 'kupwara']))
print('--'.join(['hey', 'my', 'name', 'is', 'wasif','and' , 'i', 'am', 'from', 'kupwara']))

# 3- Replace() :- Replace something in string 
print('hi my name is wasif'.replace('wasif','ahti'))

# 4- strip() :- Erases all the extra spaces in 'start / end'  of the string
print("    wasif ahmad          ".strip())