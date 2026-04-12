# WAP which can remove a perticular character from a string
# Well , we can not edit a string but we can make new string from existing one and vipe the character which is requiired to do 
s=input('Enter string :- ')
term=input('What would you like to remove :- ')
newS=''
for i in s:
    if i == term:
        continue
    else:
        newS=newS+i
    
else:
    print(newS)