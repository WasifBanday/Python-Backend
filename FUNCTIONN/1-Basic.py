def is_even(num):
    if type(num) == int:
        if num % 2 ==0 :
            return 'Even'
        else :
            return 'Odd'
    else:
        return 'pagal hai kya bhosdi'
for i in range(1,11):
    x=is_even(i)
    print(x)