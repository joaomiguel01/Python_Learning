resp = "S"
sum = cont = bigger = minor = 0
while resp not in "Nn":
    if resp in "Ss":
        num = int(input("Digite um número: "))
        sum += num
        cont += 1

        if cont == 1:
            bigger = minor = num
        else:
            if num > bigger:
                bigger = num
            elif num < minor:
                minor = num
    resp = input("Quer continuar? [S/N]: ")

print(f"\nMédia dos valores: {sum/cont:.2f}")
print(f"Maior valor é {bigger} e o menor é {minor}")
