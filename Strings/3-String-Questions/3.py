# Count the frequency of a perticuler character in provided string
s=input('Enter string :- ')
term=input('What would you like to search for :- ')
count=0
for i in s :
    if i==term:
        count+=1
print(count)