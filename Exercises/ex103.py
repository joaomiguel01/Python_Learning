def ficha(jogador, gols):
    if jogador == "":
        jogador = "<desconhecido>"
    if gols == "":
        gols = "0"
    
    print(f"O jogador {jogador} fez {gols} no campeonato")

name = input("Nome do Jogador: ")
gols = input("Número de Gols: ")
ficha(name, gols)
