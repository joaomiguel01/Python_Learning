from random import randint
vics = 0
print("Vamos Jogar um jogo de PAR ou ÍMPAR!\n")
while True:
    player = int(input("Digite um valor: "))
    choice = input("Par ou Ímpar [P/I]: ").upper()
    machine = randint(0, 10)

    total = machine + player

    if total%2 == 0:
        print(f"Jogador jogou {player} e a máquina jogou {machine}. Total de {total} deu PAR")
        if choice == "P":
            print("\nPlAYER WINS!!!\n")
            vics += 1
        else:
            print("\nPERDEU!!!!!\n")
            break
    else:
        print(f"Jogador jogou {player} e a máquina jogou {machine}. Total de {total} deu ÍMPAR")
        if choice == "I":
            print("\nPlAYER WINS!!!\n")
            vics += 1
        else:
            print("\nPERDEU!!!!!\n")
            break
print("\nGAME OVER")
print(f"Total de vitórias: {vics}")