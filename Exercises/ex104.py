def leiaInt(text):
    while True:
        num = input(text)
        if num.isnumeric():
            return int(num)
        else:
            print("\033[1;31mDADO INVÁLIDO!\033[m")

num = leiaInt("Digite um número: ")
print("Você digitou", num)
            