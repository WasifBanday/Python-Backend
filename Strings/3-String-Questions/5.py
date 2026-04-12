# WAP that can check weather a string is palindrome or not
# '/'  --> Normal division   [7/2 = 3.5]
# '//'  --> Integer division [7/2 = 3]

s=input('Enter string to check :- ')
for i in range(0,len(s)//2):
    if s[i]!=s[len(s)-i-1]:
        print("Not a palindrome")
        break
else:  # Runs only if the loop doesnt break
    print('Palindrome')