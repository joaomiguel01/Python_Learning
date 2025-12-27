from utils.moeda import aumentar, dobro, metade, formatar

def function(price):
    print(f"A metade de {formatar(price, "R$")} é {formatar(metade(price), "R$")}")
    print(f"O dobro de {formatar(price, "R$")} é {formatar(dobro(price), "R$")}")
    print(f"Aumentando em 10%, temos {formatar(aumentar(price, 10), "R$")}")

price = float(input("Digite o preço: R$"))
function(price)
