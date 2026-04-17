# Tuple Functions 
# same as list      # (Len/max/min/sum/sorted)

# Count()
t=(1,2,3,4,5,4,5,6,4,5)
print(t.count(5))

# Index()
t2=(4,5,4,5,6,4,5)
print(t.index(6))


# Zip()
a=(1,2,3,4)
b=(10,11,12,13)
print(tuple(zip(a,b)))