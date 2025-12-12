price = float(input("Digite o valor total das compras: R$"))
options = int(input("MENU: \n[1] À VISTA DINHEIRO/CHEQUE\n[2] À VISTA CARTÃO\n[3] 2X NO CARTÃO\n[4] 3X OU MAIS\nSua Escolha: "))

if options == 1:
    print(f"À vista no dinheiro/cheque, você tem 10% de desconto, totalizando R${price*0.9:.2f}")
elif options == 2:
    print(f"À vista no cartão, você tem 5% de desconto, totalizando R${price*0.95:.2f}")
elif options == 3:
    print(f"Em 2x sem juros, cada parcela será de R${price/2:.2f}")
elif options == 4:
    parcs = int(input("\nNúmero de parcelas: "))
    print(f"Em {parcs}x, com 20% de juros, cada parcela será de R${price*1.2/parcs:.2f}, totalizando R${price*1.2:.2f}")
else:
    print("DADO INVÁLIDO!")
    