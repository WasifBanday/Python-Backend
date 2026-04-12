# Slicing :- We can extract more then one character in an string

s="hello world"
print(s[0:5])

# print from 0 to 3 index
print(s[:4])  # basically this means print from 0 index upto 3  

# print from 0 to max length
print(s[0:])

# print from 2 to 4 index
print(s[2:5])

# print after one latter , means h not e , and l not second l , and so on ...
print(s[0:5:2])

# print from last to 3rd index
print(s[7:0:-1])

# Reverse the whole string 
print(s[::-1])