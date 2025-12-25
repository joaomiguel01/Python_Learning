from datetime import date
def voto(year_age):
    age = date.today().year - year_age

    if age < 16:
        rank = "NÃO VOTA"
    elif 16 <= age < 18:
        rank = "VOTO OPCIONAL"
    elif 18 <= age < 70:
        rank = "VOTO OBRIGATÓRIO"
    else:
        rank = "VOTO OPCIONAL"
    
    print(f"Você possui {age} anos: {rank}")

year = int(input("Ano de nascimento: "))
voto(year)