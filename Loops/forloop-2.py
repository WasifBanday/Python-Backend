# Question : The current population of the town is 10000 , the population of the town is increasing 10% per year ,
#            We have to write a program to find out the population at the end of each of the last 10 years 
current_population=10000
for i in range(10,0,-1):
    print(i,'th:-' , current_population)
    current_population=current_population/1.1