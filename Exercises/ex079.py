resp = "S"
nums = []
while resp not in "Nn":
    if resp in "Ss":
        num = int(input("Digite um valor: "))

        if num not in nums:
            nums.append(num)
            print("Valor adicionado com sucesso!")
        else:
            print("Valor duplicado!")
    
    resp = input("Quer continuar? [S/N]: ")

nums.sort()
print("\nNúmeros:", nums)
