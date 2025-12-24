products = ("Lápis", 1.75, "Borracha", 2, "Caderno", 15.9, "Estojo", 25)

for pos, p in enumerate(products):
    if pos%2 == 0:
        print(f"{p:.<30}", end="")
    else:
        print(f"R${p:7.2f}")