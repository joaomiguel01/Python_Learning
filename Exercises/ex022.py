from random import randint
print("==="*20)
print(f"{'JOGO DE ADIVINHAÇÃO V1.0':^60}")
print("==="*20)
print("Vou pensar em um número entre 0 e 5, tente adivinhar!")
machine = randint(0, 5)
player = int(input("Digite seu melhor palpite: "))
if player == machine:
    print(f"\nPARABÉNS!!! Você acertou o número que eu estava pensando ({machine})")
else:
    print(f"\nERRRRRRRRROU!!! O número era ({machine})")
