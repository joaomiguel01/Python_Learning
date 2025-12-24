houseval = float(input("Valor da casa: R$"))
wage = float(input("Salário: R$"))
years = int(input("Anos de financiamento: "))
pres = houseval/(years*12)

print(f"Para pagar uma casa de R${houseval:.2f} em {years} anos, a prestação será R${pres:.2f}")
if pres > 0.3*wage:
    print("EMPRÉSTIMO NEGADO!")
else:
    print("EMPRÉSTIMO APROVADO!")
