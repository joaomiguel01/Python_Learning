sum = cont = 0
while True:
    num = int(input("Digite um número [999 para parar]: "))

    if num != 999:
        sum += num
        cont += 1
    else:
        break

print(f"\nVocê digitou {cont} valor(es), totalizando {sum}")
