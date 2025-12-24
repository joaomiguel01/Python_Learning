words = ("APRENDER", "PROGRAMAR", "LINGUAGEM", "PYTHON", "CURSO")

for w in words:
    print(f"Na palavra {w} temos:", end=" ")
    for char in w:
        if char in "AEIOU":
            print(char, end=" ")
    print()