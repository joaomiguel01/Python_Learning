num = int(input("Digite um número: "))
options = int(input("MENU: \n[1] BINÁRIO\n[2] OCTAL\n[3] HEXADECIMAL\nSua Escolha: "))

if options == 1:
    print(f"Em BINÁRIO, será {bin(num)[2:]}")
elif options == 2:
    print(f"Em OCTAL, será {oct(num)[2:]}")
elif options == 3:
    print(f"Em HEXADECIMAL, será {hex(num)[2:]}")
else:
    print("DADO INVÁLIDO!")
