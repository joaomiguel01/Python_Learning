from random import randint
print("Vamos jogar um jogo de jokenpô!")

machine = randint(0, 2)
player = int(input("MENU: \n[0] PEDRA\n[1] PAPEL\n[2] TESOURA\nSua Escolha: "))
options = ("PEDRA", "PAPEL", "TESOURA")

print("-"*17)
print(f"PLAYER: {options[player]}")
print(f"MÁQUINA: {options[machine]}")
print("-"*17)

if player == 0 and machine == 2:
    print("PLAYER WINS!")
elif player == 1 and machine == 0:
    print("PLAYER WINS!")
elif player == 2 and machine == 1:
    print("PLAYER WINS!")
elif player == machine:
    print("EMPATE!!!")
else:
    print("PERDEU OTÁRIO!!!!!")
    