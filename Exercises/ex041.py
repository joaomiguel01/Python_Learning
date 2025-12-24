from datetime import date
year_age = int(input("Ano de nascimento: "))
age = date.today().year - year_age

if age <= 9:
    rank = "MIRIM"
elif age <= 14:
    rank = "INFANTIL"
elif age <= 19:
    rank = "JÚNIOR"
elif age <= 25:
    rank = "SÊNIOR"
else:
    rank = "MASTER"

print(f"Você tem {age} anos e você é {rank}")