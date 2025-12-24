from random import randint
print("Vou pensar em um número entre 0 e 5, tente adivinhar!")
machine = randint(0, 5)
player = int(input("Digite seu melhor palpite: "))

if player == machine:
    print(f"PARABÉNS!!! Você acertou o número ({machine})")
else:
    print(f"ERRRRRRRRROU!!!! O número era ({machine})")
    