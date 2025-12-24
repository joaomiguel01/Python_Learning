from random import randint
print("Vou pensar em um número entre 0 e 10, tente adivinhar!")
machine = randint(0, 10)
player = int(input("Digite seu melhor palpite: "))
palps = 1

while player != machine:
    if player < machine:
        player = int(input("ERRRRRRROU!!! Chute mais alto: "))
    elif player > machine:
        player = int(input("ERRRRRRROU!!! Chute mais baixo: "))
    palps += 1

print(f"PARABÉNS!!! Você acertou o número ({machine}) em {palps} palpite(s)")
