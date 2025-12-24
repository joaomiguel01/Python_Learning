sum = cont = 0
for c in range(1, 501, 2):
    if c%3 == 0:
        sum += c
        cont += 1

print(f"Foram solicitados {cont} valores, totalizando {sum}")