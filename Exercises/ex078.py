nums = []
for c in range(0, 5):
    num = int(input(f"Digite um número na posição {c}: "))
    nums.append(num)

print("\nValores:", nums)
print(f"O maior valor é {max(nums)} nas posições:", end=" ")
for p, n in enumerate(nums):
    if n == max(nums):
        print(p, end="... ")
print()

print(f"O menor valor é {min(nums)} nas posições:", end=" ")
for p, n in enumerate(nums):
    if n == min(nums):
        print(p, end="... ")
print()
