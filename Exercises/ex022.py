from random import randint
from time import sleep
print("=="*30)
print(f"{'JOGO DE ADIVINHAÇÃO V1.0':^60}")
print("=="*30)
print("Vou pensar em um número entre 0 e 5, tente adivinhar!")
print("PENSANDO...")
sleep(2)

machine = randint(0, 5)
player = int(input("PENSEI!!! Digite seu melhor palpite: "))

if player == machine:
    print("\nPARABÉNS!!! Você acertou o número que eu estava pensando!")
else:
    print(f"\nERRRRRRRRRROU!!!! O número era {machine}")
