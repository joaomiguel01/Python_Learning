data = []
persons = []
resp = "S"
bigger = minor = 0
while resp not in "Nn":
    if resp in "Ss":
        name = input("Nome: ")
        weight = float(input("Peso: "))
        data.append(name)
        data.append(weight)

        persons.append(data[:])
        
        if len(persons) == 1:
            bigger = minor = weight
        else:
            if weight > bigger:
                bigger = weight
            elif weight < minor:
                minor = weight
        data.clear()


    resp = input("Quer continuar? [S/N]: ")

print("\nTotal de pessoas:", len(persons))
print(f"Maior peso foi {bigger:.2f}kg com:", end=" ")
for p in persons:
    if p[1] == bigger:
        print(f"[{p[0]}]", end=" ")
print()

print(f"Menor peso foi {minor:.2f}kg com:", end=" ")
for p in persons:
    if p[1] == minor:
        print(f"[{p[0]}]", end=" ")
print()
