from datetime import date
year_age = int(input("Digite o ano de nascimento: "))
atual = date.today().year
age = atual - year_age

print(f"Você tem {age} anos em {atual}")
if age < 18:
    print(f"Ainda faltam {18-age} anos para você se alistar em {atual+(18-age)}")
elif age == 18:
    print("Aliste-se imediatamente")
else:
    print(f"Você já se alistou há {age-18} anos em {atual-(age-18)}")
    