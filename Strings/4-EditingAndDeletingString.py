# Editing :- In python string is immutable , which means editing a string is not allowed , once decleared

# Deleting a string . 
s='hello'
del s  # del removes the variable reference , not the object itself , python's garbage collector frees the memory once no reference remain
print(s)



# Question : What will be the output
strr='hello world'
del s[-1:-5:2]
print(strr)    # Error Because we are trying to delete a portion from a string which is not allowed , because we can't edit a string in .py