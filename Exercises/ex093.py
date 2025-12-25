data = dict()
data['nome'] = input("Nome do Jogador: ")
num_parts = int(input("Número de Partidas: "))
gols = []
for c in range(num_parts):
    gol = int(input(f"Gols da partida {c}: "))
    gols.append(gol)
data['gols'] = gols
data['total'] = sum(gols)
print(data)
