sum_age = old_man = y_womens = 0
old_man_name = ""
for c in range(1, 5):
    name = input("Nome: ")
    age = int(input("Idade: "))
    sex = input("Sexo [M/F]: ")

    sum_age += age

    if sex in "Mm":
        if age > old_man:
            old_man = age
            old_man_name = name
    elif sex in "Ff" and age < 20:
        y_womens += 1

print(f"\nA média de idade: {sum_age/4:.2f} anos")
print(f"O homem mais velho tem {old_man} anos e se chamava {old_man_name}")
print(f"Existem {y_womens} mulheres com menos de 20 anos")
