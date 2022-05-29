from ast import And
from random import randint, random
import sys

answer= randint(1,10)

while True:
    
    try:
        guess= int(input("Enter number from 1-10"))
        if guess==answer:
            print("You guess right")
            print("thanks for playing")
            break

        elif guess<0 or guess>10:
            print("you have not entred number from 1-10")
            continue
        else:
            print("wrong guess")
            print("try again")
            continue
 
    except ValueError:
        print("please type number from 1-10")
        continue
