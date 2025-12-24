num = int(input("Digite um número: "))
fact = 1
for c in range(num, 0, -1):
    fact *= c
print(f"{num}! = {fact}")