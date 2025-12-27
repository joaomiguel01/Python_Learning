from utils.moeda import aumentar, dobro, metade

def function(price):
    print(f"A metade de {price:.2f} é {metade(price):.2f}")
    print(f"O dobro de {price:.2f} é {dobro(price):.2f}")
    print(f"Aumentando em 10%, temos {aumentar(price, 10):.2f}")

price = float(input("Digite o preço: R$"))
function(price)
