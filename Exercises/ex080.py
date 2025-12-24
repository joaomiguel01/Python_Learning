nums = []
for c in range(0, 5):
    num = int(input("Digite um número: "))
    if len(nums) == 0 or num > max(nums):
        nums.append(num)
        print("Valor adicionado ao final da lista!")
    else:
        for p, n in enumerate(nums):
            if num <= n:
                nums.insert(p, num)
                print(f"Valor adicionado na posição {p}")
                break
print("Valores ordenados:", nums)