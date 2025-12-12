houseval = float(input("Valor da casa: R$"))
wage = float(input("Salário do funcionário: R$"))
years = int(input("Anos de financiamento: "))
pres = houseval/(years*12)

print(f"PARA FINANCIAR UMA CASA DE R${houseval:.2f} em {years} anos, a prestação será de R${pres:.2f}")
if pres > 0.3*wage:
    print("EMPRÉSTIMO NEGADO!")
else:
    print("EMPRÉSTIMO APROVADO!")
