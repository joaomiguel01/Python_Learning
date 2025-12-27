from utils.moeda import aumentar, dobro, metade, formatar

def function(price):
    print(f"A metade de {formatar(price, "R$")} é {metade(price, True)}")
    print(f"O dobro de {formatar(price, "R$")} é {dobro(price, True)}")
    print(f"Aumentando em 10%, temos {aumentar(price, 10, True)}")

price = float(input("Digite o preço: R$"))
function(price)
