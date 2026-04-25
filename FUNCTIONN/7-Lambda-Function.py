# A lambra function is a small anonymous function 
# A lambda function can take any number of arguments , but can have only one expression .
# lambda function has no name  
# Lambda has no return value ( infact , it returns a function itself )
# Lambda is written in 1 line 
# No reusability

lambda a,b:a+b # Normal expression 

# Example 1
a=lambda x:x**2
print(a(2))

# Example 2
a=lambda x,y:x+y
print(a(5,2))

# Lambda function are used with HOF [ higher order function ]

# Question : check if a string has 'a'
string=lambda s:'a' in s
print(string('hello'))

# Question : check even or odd 
a=lambda x : 'Even' if x%2==0 else 'Odd'
print(a(4))