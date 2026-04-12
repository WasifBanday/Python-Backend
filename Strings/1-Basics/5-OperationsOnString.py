# Arithematic Operations 
# 1- CAn add string 
print('delhi'+' '+'mumbai')
# 2- Can multiply string 
print('delhi '*5)


# Relational Operations
#  We Can compare the string values Based on Its 'ASCII' values
print('kashmir'=='kashmir')
print('kashmir'!='kashmir')
print('KASHMIR'>'kashmir')
print('KASHMIR'<'kashmir')


# Logical Operations 
#  If the string has nothing in it it is taken as "False" , and if its filled then its taken as "True"
# "and" this operator checks both the condition an prints last "true"
print('hello' and 'world')
# "or" this checks the nearest "True" and prints that
print('hello' or 'world')


# Loops In string
# Strings in python are iterable , means they can be iterated using loop
for i in ('hello'):
    print(i)
for i in ('Kashmir'):
    print('Kupwara')
    
    
# Membership Operatons
# "In" an "not in" :- Both are use to check the conditions , and returns true false
print('K' in 'Kashmir')
print('K' not in 'Kashmir')