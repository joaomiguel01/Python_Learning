num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
options = 0
while options != 5:
    options = int(input("\nMENU: \n[1] SOMAR\n[2] MULTIPLICAR\n[3] SABER O MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA\nSua Escolha: "))

    if options == 1:
        print(f"\nA soma entre {num1} e {num2} é igual a {num1+num2}\n")
    elif options == 2:
        print(f"\nO produto entre {num1} e {num2} é igual a {num1*num2}\n")
    elif options == 3:
        if num1 > num2:
            print(f"\n{num1} é maior que {num2}\n")
        elif num2 > num1:
            print(f"\n{num2} é maior que {num1}\n")
        else:
            print(f"\nOs dois são iguais\n")
    elif options == 4:
        num1 = int(input("\nPrimeiro número: "))
        num2 = int(input("Segundo número: "))
    elif options < 0 or options > 5:
        print("\nDADO INVÁLIDO!\n")

