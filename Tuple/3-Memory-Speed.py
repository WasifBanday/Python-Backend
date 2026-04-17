# Proof that tuple take less memory then list

import sys
L=list(range(10000000))
T=tuple(range(10000000))
print('list size',sys.getsizeof(L))
print('tuple size',sys.getsizeof(T))

# Proof that tuples are faster then list
import time
L1=list(range(10000000))
T1=tuple(range(10000000))
start=time.time()
for i in L1 :
    i*5
print('list time',time.time()-start)

start=time.time()
for i in T1 :
    i*5
print('tuple time',time.time()-start)