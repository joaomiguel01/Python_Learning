from Exercises.ex115.dado import leiaDinheiro
from utils.moeda import resumo

def main():
    price = leiaDinheiro("Digite o preço: R$")
    resumo(price, 35, 22)


if __name__ == "__main__":
    main()