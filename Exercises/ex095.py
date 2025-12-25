resp = "S"
data = {}
players = []
gols = []
while resp not in "Nn":
    if resp in "Ss":
        data['nome'] = input("Nome do Jogador: ")
        num_parts = int(input("Número de partidas: "))
        for c in range(num_parts):
            gol = int(input(f"Quantos gols na partida {c+1}: "))
            gols.append(gol)
        data['gols'] = gols[:]
        data['total'] = sum(gols)

        players.append(data.copy())
        data.clear()
        gols.clear()
        
    resp = input("Quer continuar? [S/N]: ")

print(f"{'ID':^3} {'NOME':<30} {'GOLS':<15} {'TOTAL':<7}")
print("-"*50)
for pos, p in enumerate(players):
    print(f"{pos:<3} {p['nome']:<30} {str(p['gols']):<15} {str(p['total']):<7}")

while True:
    option = int(input("Mostrar dados de qual jogador? (999 para parar): "))
    if option == 999:
        break
    elif not (0 <= option < len(players)):
        print("DADO INVÁLIDO!")
    else:
        print(f"\nLEVANTAMENTO DO JOGADOR {players[option]['nome']}:")
        for c in range(len(players[option]['gols'])):
            print(f"\tNo jogo {c+1} fez {players[option]['gols'][c]} gols.")
        print("")