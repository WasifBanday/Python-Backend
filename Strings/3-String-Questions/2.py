# Extract User name from email , 
# If the email is like wasif121@gamil.com , we have to extract only wasif121

s=input('Enter your email :- ')
position=s.index('@')
print(s[0:position])