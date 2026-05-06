# filter - >  given list mai , eik condition k basis pa kaam karna 

# Example :  find , numbers greater then 5 in a list ?

l=[1,2,4,5,7,8,9,5,8]
print(list(filter(lambda x : x > 5 , l)))

# Example : Fetch fruits starting with 'a'
fruits=['apple','guava','cherry']
print(list(filter(lambda x:x.startswith('a'),fruits)))