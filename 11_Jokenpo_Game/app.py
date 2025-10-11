# Python jokenpo game program

from random import choice

options = ("rock", "paper", "scissors")

player = None
computer = choice(options)
is_running = True

while is_running:        
    while player not in options:
        player = input("Enter choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    if not input("Play again? (y/n)".lower == "y"):
        break

print("Thanks for playing!")
