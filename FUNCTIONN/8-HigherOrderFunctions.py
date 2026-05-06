# The type of functions which returns another function , or which receives another function as input 

def transform (f,l):
    output=[]
    for i in l :
        output.append(f(i))
    print(output)
l=[1,2,3,4,5]
transform(lambda x : x**2 , l)  # This is equal to 'f' in def function .