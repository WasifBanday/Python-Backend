# WAP to convert a string title case without using title method/function

s=input("Enter string :- ")
L=[]
for i in s.split():
    L.append(i[0].upper()+i[1:].lower())
print(' '.join(L))