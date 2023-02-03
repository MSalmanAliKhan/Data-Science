# Number guessing game
from random import random
winning_number= random()
guessed_number=int(input("Guess a number to see to play the game"))
if winning_number==guessed_number:
    print("You win")
else:
    if winning_number<guessed_number:
        print("Too high")
    else:
        print("Too low")
