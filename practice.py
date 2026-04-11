# n = int(input("Enter n "))
# result=0
# for i in range(0,n+1):
#     result=result+i
# print(result)
n = int (input('Enter n :- '))
for i in range(1,n+1):
    for j in range(1,i+2):
        for k in range(1,j+1):
            print(k,end='')
        print()
    print()