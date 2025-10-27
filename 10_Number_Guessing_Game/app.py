# Python Number Guessing Game

import random

low_num = 1
high_num = 100
answer = random.randint(low_num, high_num)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {low_num} and {high_num}")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < low_num or guess > high_num:
            print("\nThat number is out of range\n")
            print(f"Please select a number between {low_num} and {high_num}\n")
        elif guess < answer:
            print("\nToo low! Try again!\n")
        elif guess > answer:
            print("\nToo high! Try again!\n")
        else:
            print(f"\nCORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False

    else:
        print("\nInvalid guess!")
        print(f"Please select a number between {low_num} and {high_num}\n")
