evens = []
odds = []
for c in range(1, 8):
    num = int(input(f"Digite um valor na posição {c}: "))

    if num%2 == 0:
        evens.append(num)
    else:
        odds.append(num)

evens.sort()
print("Valores pares:", evens)
odds.sort()
print("Valores ímpares:", odds)
