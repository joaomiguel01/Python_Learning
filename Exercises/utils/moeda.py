def aumentar(price, tax, form=True):
    val = price*(1+tax/100)
    return val if form == False else formatar(val, "R$")


def diminuir(price, tax, form=True):
    val = price*(1-tax/100)
    return val if form == False else formatar(val, "R$")


def dobro(price, form=True):
    val =  price*2
    return val if form == False else formatar(val, "R$")


def metade(price, form=True):
    val =  price/2
    return val if form == False else formatar(val, "R$")


def resumo(price, tax_aumento, tax_desconto):
    print("~"*30)
    print(f"{'RESUMO DO VALOR':^30}")
    print("~"*30)
    print(f"Preço analisado: \t{formatar(price, 'R$')}")
    print(f"Dobro do preço:  \t{dobro(price)}")
    print(f"Metade do preço: \t{metade(price)}")
    print(f"{tax_aumento} de aumento:   \t{aumentar(price, tax_aumento)}")
    print(f"{tax_desconto} de redução:   \t{diminuir(price, tax_desconto)}")
    


def formatar(price, symbol):
    return f"{symbol}{price:.2f}".replace(".", ",")