# Find sequence sum of the terms till nth term , nth term entered by user ,, 1/1! + 2/2! + 3/3! + ... n/n!
n=int(input('Enter nth term :- '))
result=0
fact=1
for i in range(1,n+1):
    fact=fact*1
    result=result+i/fact
print(result)