#random no guess

import random

target = random.randint(1,1000)
count=0
while True: 
    guess=input(" GUESS THE CORRECT NO or press Q to QUIT ")
    count+=1

    if(guess=="Q"or guess=="q"):
        print("----YOU LOST----")
        break

    guess=int(guess)

    if (guess==target):
        print("BOOYAH! yor're correct ")
        print("you took ---",count,"--- steps to win .")
        break

    elif (guess<target):
        print("you guessed a little less, Try Again ")

    else :
        print("you guessed a little more, Try Again ")

print("----GAME OVER----")