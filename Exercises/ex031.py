number = int(input("Digite um número: "))
options = int(input("MENU: \n[1] BINÁRIO \n[2] OCTAL \n[3] HEXADECIMAL \nSua Escolha: "))

if options == 1:
    print(f"{number}, em BINÁRIO, será {bin(number)[2:]}")
elif options == 2:
    print(f"{number}, em OCTAL, será {oct(number)[2:]}")
elif options == 3:
    print(f"{number}, em HEXADECIMAL, será {hex(number)[2:]}")
else:
    print("DADO INVÁLIDO!")

