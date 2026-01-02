# GUI utilities
colors = {'transparent': "\033[m",
          "red": "\033[1;31m",
          "green": "\033[1;32m",
          "yellow": "\033[1;33m",
          "blue": "\033[1;36m"}


# GUI Functions
def title(text: str):
    print("~"*(len(text)+4))
    print(f"  {text}")
    print("~"*(len(text)+4))


def menu():
    text = "SISTEMA DE CADASTRO DE USUÁRIOS"
    title(text)

    options = [
        "Cadastrar Usuários",
        "Ver Usuários",
        "Deletar Usuários",
        "Atualizar Usuários",
        "Sair do Programa"
    ]

    for index, option in enumerate(options, start=1):
        print(f"{colors['yellow']}[{index}]{colors['transparent']} {colors['blue']}{option}{colors['transparent']}")
    
    print('~'*(len(text)+4))


# Command utils
def read_option(text: str, max_value_options: int):
    while True:
        try:
            num = int(input(text))
            if 1 <= num <= max_value_options:
                return num
            else:
                print(f"{colors['red']}Dado Inválido! Digite uma opção válida!{colors['transparent']}")
        except ValueError:
            print(f"{colors['red']}Dado Inválido! Digite um número!{colors['transparent']}")
