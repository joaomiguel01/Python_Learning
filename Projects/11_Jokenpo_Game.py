# Python Jokenpo Game

from random import choice
options = ("rock", "paper", "scissors")
is_running = True

while is_running:

    player = None
    computer = choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("Player wins!")
    elif player == "paper" and computer == "rock":
        print("Player wins!")
    elif player == "scissors" and computer == "paper":
        print("Player wins!")
    else:
        print("Computer wins!")
    

    if not input("Play again? [Y/N]: ").upper() == "Y":
        is_running = False