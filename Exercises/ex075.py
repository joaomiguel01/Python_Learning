numbers = (int(input("Digite um número: ")), int(input("Digite um número: ")),
           int(input("Digite um número: ")), int(input("Digite um número: ")))

print("\nValores:", numbers)
print(f"O valor 9 apareceu {numbers.count(9)} vez(es)")
if 3 in numbers:
    print("O valor 3 apareceu na posição", numbers.index(3)+1)
else:
    print("O valor 3 não apareceu!")

evens = 0
for n in numbers:
    if n%2 == 0:
        evens += 1

print("Total de valores pares:", evens)
