from datetime import date
olds = youngs = 0
for c in range(1, 8):
    year_age = int(input(f"Ano de nascimento da {c}º pessoa: "))
    age = date.today().year - year_age

    if age > 21:
        olds += 1
    else:
        youngs += 1

print("Maiores de idade:", olds)
print("Menores de idade:", youngs)
