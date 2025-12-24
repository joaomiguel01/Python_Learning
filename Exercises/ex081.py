nums = []
resp = "S"
while resp not in "Nn":
    if resp in "Ss":
        num = int(input("Digite um valor: "))
        nums.append(num)
    resp = input("Quer continuar? [S/N]: ")

print("\nTotal de elementos:", len(nums))
nums.sort(reverse=True)
print("Valores em ordem decrescente:", nums)
if 5 in nums:
    print(f"Valor 5 faz parte da lista")
else:
    print(f"Valor 5 não faz parte da lista")
