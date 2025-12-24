nums = []
evens = []
odds = []
resp = "S"
while resp not in "Nn":
    if resp in "Ss":
        num = int(input("Digite um número: "))
        nums.append(num)

        if num%2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    resp = input("Quer continuar? [S/N]: ")

print("\nValores:", nums)
print("Números pares:", evens)
print("Números Ímpares:", odds)
