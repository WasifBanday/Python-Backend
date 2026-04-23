# Types Of Arguments 

# 1 :- Default Arguments [ Setting default values in a parament] [ Used to prevent from an error , If you pas less arguemnts or no agrument ]
def power(a=1,b=2):
    return a**b
print(power())
print(power(2))
print(power(2,3))

# 2 :- Positional Argument [Jis order mai aap arguments ko bejoge usi order mai parameter unko receive krega]
# example
print(power(4,5)) # a=4 and b=5 [simple default behaviour]

# 3 :- Keyword Argument [ Passing argument direct to parameter names]
print(power(b=3,a=2))