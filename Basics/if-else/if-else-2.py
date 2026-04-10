# Find max of three numbers entered by user
a=int(input('Enter 1st number :- '))
b=int(input('Enter 2nd number :- '))
c=int(input('Enter 3rd number :- '))
if a>b and a>c:
    print('a is greater ')
elif b>c :
    print('b is greater')
elif a==b and a==c and c==b:
    print('a=b=c , all are equal')
else:
    print('c is greater')