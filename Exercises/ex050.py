sum = 0
for c in range(1, 7):
    num = int(input(f"Digite o {c}º número: "))
    if num%2 == 0:
        sum += num

print(f"A soma dos valores pares será igual a {sum}")