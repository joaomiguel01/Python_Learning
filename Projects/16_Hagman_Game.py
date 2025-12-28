# Python Hangman Game

from random import choice

words = ("apple", "orange", "banana", "coconut", "pineapple")

# Dictionary of key: ()
hangman = {0: ("   ",
               "   ",
               "   "),
           1: (" o ",
               "   ",
               "   "),
           2: (" o ",
               " | ",
               "   "),
           3: (" o ",
               "/| ",
               "   "),
           4: (" o ",
               "/|\\",
               "   "),
           5: (" o ",
               "/|\\",
               "/  "),
           6: (" o ",
               "/|\\",
               "/ \\")}

def display_man(wrong_guesses):
    print("~"*30)
    for line in hangman[wrong_guesses]:
        print(line)
    print("~"*30)


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))



def main():
    answer = choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if guess == answer[i]:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False
        elif wrong_guesses >= len(hangman) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False

if __name__ == "__main__":
    main()
