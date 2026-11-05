#guess the number

import random

number =random.randint(1, 10)


while True:
    guess = int(input("Guess a Number from 1 to 10..."))
    
    if guess < number:
        print("Too Low")
       
    elif guess > number:
        print("Too High")

    else:
        print("Correct! You guessed it!")
      
