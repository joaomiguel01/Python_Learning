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


def menu(title_text: str, options_list: list):
    title(title_text)

    for index, option in enumerate(options_list, start=1):
        print(f"{colors['yellow']}[{index}]{colors['transparent']} {colors['blue']}{option}{colors['transparent']}")
    
    print('~'*(len(title_text)+4))


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


def read_name(text: str):
    while True:
        try:
            name = input(text)
            if name.strip():
                return name.strip()
            else:
                print(f"{colors['red']}ERROR! Digite um nome válido!{colors['transparent']}")
        except Exception as e:
            print(f"{colors['red']}ERRO: {e}{colors['transparent']}")


def read_int(text: str):
    while True:
        try:
            num = input(text)
            return int(num)
        except Exception as e:
            print(f"{colors['red']}ERRO: {e}{colors['transparent']}")


def read_float(text: str):
    while True:
        try:
            num = input(text).replace(",", ".")
            return float(num)
        except Exception as e:
            print(f"{colors['red']}ERRO: {e}{colors['transparent']}")
