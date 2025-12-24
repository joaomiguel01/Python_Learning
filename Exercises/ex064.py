num = 0
sum = cont = 0
while num != 999:
    num = int(input("Digite um número [999 para parar]: "))
    if num != 999:
        sum += num
        cont += 1
print(f"\nVocê digitou {cont} valores, totalizando {sum}")
