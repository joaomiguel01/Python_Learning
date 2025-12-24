resp = "S"
plus_18 = mans = y_womens = 0
while resp not in "Nn":
    if resp in "Ss":
        age = int(input("Idade: "))
        sex = input("Sexo [M/F]: ")

        if age > 18:
            plus_18 += 1
        
        if sex in "Mm":
            mans += 1
        elif sex in "Ff" and age < 20:
            y_womens += 1
    
    resp = input("Quer continuar? [S/N]: ")

print("\nPessoas com mais de 18 anos:", plus_18)
print("Total de homens cadastrados:", mans)
print("Total de mulheres com menos de 20 anos:", y_womens)