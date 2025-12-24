resp = "S"
data = []
persons = []
while resp not in "Nn":
    if resp in "Ss":
        name = input("Nome: ")
        note1 = float(input("Nota 1: "))
        note2 = float(input("Nota 2: "))
        media = (note1+note2)/2

        data.append(name)
        data.append(note1)
        data.append(note2)
        data.append(media)
        persons.append(data[:])
        data.clear()

    resp = input("Quer continuar? [S/N]: ")


print(f"\n{'ID':<3} {'NOME':<25} {"MÉDIA":<7}")
print("-"*40)
for pos, person in enumerate(persons):
    print(f"{pos:<3} {person[0]:<25} {person[3]:<7.2f}")

while True:
    option = int(input("\nMostrar notas de qual aluno? (999 para parar): "))

    while not (0 <= option < len(persons)) and option != 999:
        option = int(input("\nDADO INVÁLIDO! Mostrar notas de qual aluno? (999 para parar): "))
    
    if option != 999:
        print(f"\nNotas de {persons[option][0]}: [{persons[option][1]}, {persons[option][2]}]")
    else:
        break        
