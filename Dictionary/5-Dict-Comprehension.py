# {key : value for vars in iterable} 
# Problem  :- print 1st 10 numbers with their squares 
print({i:i**2 for i in range(1,11)})

# Problem :- Using .zip  
days ={ 'monday','tuesday','wednesday','thursday','friday','saturday','sunday'}
temp_c={30.1,32.2,33.2,34.5,32.4,34,35.2}
print({i:j for (i,j) in zip(days,temp_c)})

# Problem :- print table of numbers from 2 to 4
print({i:{j:i*j for j in range(1,11)} for i in range(2,5)})