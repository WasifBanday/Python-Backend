# print triangle pattern , length of triangle is entered by user

rows=int(input('Enter no of rows:- '))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(' * ',end='')
    print()