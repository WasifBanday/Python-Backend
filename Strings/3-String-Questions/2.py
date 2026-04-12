# Extract User name from email , 
# If the email is like wasif121@gamil.com , we have to extract only wasif121

str=input('Enter your email :- ')
position=str.index('@')
print(str[0:position])