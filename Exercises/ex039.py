from random import randint
from time import sleep

print("=="*30)
print(f"{'JOKENPÔ V1.0':^60}")
print("=="*30)
print("Vamos jogar um jogo de JOKENPÔ, tente ganhar de mim!")

machine = randint(0, 2)
player = int(input("MENU: \n[0] PEDRA\n[1] PAPEL\n[2] TESOURA\nSua Escolha: "))
options = ["PEDRA", "PAPEL", "TESOURA"]

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ!!!\n")
sleep(1)

print("-"*17)
print("JOGADOR:", options[player])
print("MÁQUINA:", options[machine])
print("-"*17)

if player == 0 and machine == 2:
    print("JOGADOR VENCEU A PARTIDA!")
elif player == 1 and machine == 0:
    print("JOGADOR VENCEU A PARTIDA!")
elif player == 2 and machine == 1:
    print("JOGADOR VENCEU A PARTIDA!")
elif player == machine:
    print("EMPATE SUPREMO")
else:
    print("PERDEEEEEEEEUUUUUUU!!!! EU SOU O CAMPEÃO DO MUNDO")