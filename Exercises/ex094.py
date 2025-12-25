resp = "S"
data = {}
persons = []
sum = 0
while resp not in "Nn":
    if resp in "Ss":
        data['nome'] = input("Nome: ")
        while True:
            data['sexo'] = input("Sexo [M/F]: ")
            if data['sexo'] in "MmFf":
                break
        data['idade'] = int(input("Idade: "))

        sum += data["idade"]
        persons.append(data.copy())
        data.clear()

    resp = input("Quer continuar? [S/N]: ")

print("\nTotal de pessoas:", len(persons))
print("Média das idades:", sum/len(persons))
print("Mulheres cadastradas:", end=" ")
for p in persons:
    if p['sexo'] in "Ff":
        print(p['nome'], end=", ")
print()

print("Pessoas acima da média: ")
for p in persons:
    if p['idade'] > (sum/len(persons)):
        print(f"nome = {p['nome']}; sexo = {p['sexo'].upper()}; idade = {p['idade']}")
