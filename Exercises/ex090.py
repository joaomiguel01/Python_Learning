data = {}
data['nome'] = input("Nome: ")
data['media'] = float(input(f"Média de {data['nome']}: "))
if data['media'] < 5:
    data['situacao'] = "Reprovado"
elif data['media'] < 7:
    data['situacao'] = "Recuperação"
else:
    data['situacao'] = "Aprovado"

print()
for key, val in data.items():
    print(f"{key} é igual a {val}")