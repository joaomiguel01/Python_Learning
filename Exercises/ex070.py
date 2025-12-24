resp = "S"
total = cont = plus_1000 = cheap = 0
cheap_name = ""
while resp not in "Nn":
    if resp in "Ss":
        name = input("Nome do Produto: ")
        price = float(input("Preço: R$"))

        total += price
        cont += 1

        if price > 1000:
            plus_1000 += 1
        
        if cont == 1:
            cheap = price
            cheap_name = name
        else:
            if price < cheap:
                cheap = price
                cheap_name = name

    resp = input("Quer continuar? [S/N]: ")

print(f"\nTotal: R${total:.2f}")
print("Total de produtos custando mais de R$1000:", plus_1000)
print(f"O produto mais barato é a {cheap_name} custando R${cheap:.2f}")