# Modified Guessing game where number of tries are also measured
from random import randint
Winning_number=randint(0,100)
guess=1
game_over=True
while game_over:
 Guessed_number=int(input("Guess the number to win: "))
 if Winning_number==Guessed_number:
    print("You win")
    if guess==1:
     print(f"You guessed in {guess} try")
    else:
        print(f"You guessed in {guess} tries")
    game_over=False
 else:
   if Guessed_number<Winning_number:
    print("Too low")
   else:
    print("Too high")
   guess+= 1
    continue


