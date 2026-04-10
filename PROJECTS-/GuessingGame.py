import random
jackpot=random.randint(1,100)
guess=int(input('Guess the number :- '))
counter=1

while guess!=jackpot:
    if guess < jackpot:
        print('Nahh , Guess higher')
    else:
        print('Nahh , Guess Lower')
    guess=int(input('Guess Again :- '))
    counter+=1
else:
    print('Yuhuuuu , Correct guess')
    print('Attempts :- ' , counter)