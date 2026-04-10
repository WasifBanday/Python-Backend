# Operator Question 
# Find the sum of three digit number entered by user
number=int(input('Enter 3 digit number:- '))

a=number%10
number=number//10

b=number%10
number=number//10

c=number%10

print('sum of entered 3 digits is', a+b+c)