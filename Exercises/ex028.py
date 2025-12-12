wage = float(input("Digite o salário do funcionário: R$"))
if wage <= 1250:
    print(f"O trabalhador que ganhava R${wage:.2f}, com 15% de aumento, passará a ganhar R${wage*1.15:.2f}")
else:
    print(f"O trabalhador que ganhava R${wage:.2f}, com 10% de aumento, passará a ganhar R${wage*1.1:.2f}")

