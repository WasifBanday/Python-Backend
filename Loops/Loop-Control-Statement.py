# 1--- Break 
# Linear searching is an example of break  
for i in range(1,11):
    if i==5:
        break
    print(i)
    
# Question :- Find the prime numbers between 2 numbers entered by the user 
lower = int(input('Enter Lower number :- '))
upper = int(input('Enter Upper number :- '))
for i in range(lower,upper+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)