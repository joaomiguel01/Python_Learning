num = int(input("Digite um número inteiro positivo: "))
divs = 0
for c in range(1, num+1):
    if num%c == 0:
        divs += 1

if divs == 2:
    print(f"{num} é PRIMO")
else:
    print(f"{num} não é PRIMO")
