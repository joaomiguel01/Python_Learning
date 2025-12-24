wage = float(input("Digite o salário: R$"))
if wage > 1250:
    print(f"Seu novo salário, com 10% de aumento, será R${wage*1.1:.2f}")
else:
    print(f"Seu novo salário, com 15% de aumento, será R${wage*1.15:.2f}")

