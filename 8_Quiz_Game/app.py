# Python Quiz Game

questions = ("How many elements in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in the Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_number = 0

for q in questions:
    print("-"*30)
    print(q)
    for o in options[question_number]:
        print(o)
    

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
        score += 1
        print("\nCORRECT!\n")
    else:
        print("\nINCORRECT!")
        print(f"{answers[question_number]} is the correct answer!\n")
    question_number += 1

print("-"*30)
print(f"{'RESULTS':^30}")
print("-"*30)

print("answers: ", end="")
for a in answers:
    print(a, end=" ")
print()

print("guesses: ", end="")
for g in guesses:
    print(g, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")