#Rock Paper Scissors

import random

choices = ['rock', 'paper', 'scissors']

user = input("Choose rock, paper, or scissors: ").lower()
computer = random.choice(choices)

print(f"You chose {user}, computer chose {computer}.")

if user == computer:
    print("It's a tie!")
elif (user == 'rock' and computer == 'scissors') or \
     (user == 'paper' and computer == 'rock') or \
     (user == 'scissors' and computer == 'paper'):
    print("You win!")
else:
    print("Computer wins!")
