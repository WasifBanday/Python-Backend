# WAP that can convert an integer into string
 
number = int(input("Enter number :- "))
digit='0123456789'
result=''

while number !=0:
    result = digit[number % 10] + result
    number=number//10
print(result)
print(type(result))