def leiaDinheiro(text: str):
    while True:
        try:
            val = input(text).strip().replace(",", ".")
            val = float(val)
            return val
        except Exception:
            print(f"\033[1;31mERRO: '{val}' não é válido!\033[m")


def leiaInt(text: str):
    while True:
        try:
            return int(input(text))
        except ValueError:
            print("\033[1;31mDADO ÍNVÁLIDO! Digite um número inteiro válido!\033[m")


def leiaReal(text):
    while True:
        try:
            val = input(text).strip().replace(",", ".")
            return float(val)
        except Exception:
            print("DADO ÍNVÁLIDO! Digite um número real válido!")