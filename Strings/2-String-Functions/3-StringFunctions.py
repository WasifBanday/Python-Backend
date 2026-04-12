# 1-count :- Tells us how many times some-thing came in string
print('my name is wasif , i am from kashmir'.count('i'))

# 2-find :- Helps u to find index number of a perticuler thing {it returns -1 , if the thing is not present in that string}
print('my name is wasif , i am from kashmir'.find('from'))

# 3-index :- same as find , but returns error if the thing is not present

# 4-endswith :- Tells us true or false if something ends with given input
print('my name is wasif , i am from kashmir'.endswith('kashmir'))

# 5-startswith :- Tells us true or false if something starts with given input
print('my name is wasif , i am from kashmir'.startswith('my'))

# 6- FORMAT  :- Help us to insert variable value into a string
name='wasif'
state='kashmir'
print('My name is {} and i am from {}'.format(name,state))

            # We can use self indexing as well ....
gender='male'
hobby='cricket'
print('My hobby is playing {1} , My gender is {0}'.format(gender,hobby))