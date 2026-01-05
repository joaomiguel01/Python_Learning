from gui_utils import title, menu, read_option
from time import sleep
from database import ensure_exists_file

def main():

    ensure_exists_file("database.json")
    title("ARQUIVO CARREGADO COM SUCESSO!")
    sleep(1)

    while True:
        try:
            print()
            menu("SISTEMA DE SUPERMERCARDO", ["Cadastrar Produto",
                                              "Ver Produtos Cadastrados",
                                              "Deletar Produto",
                                              "Atualizar Produto",
                                              "Sair do Programa"])
            print()
            choice = read_option("Digite a opção desejada: ", 5)
            sleep(1)

            match choice:
                case 1:
                    # Register Product
                    pass
                case 2:
                    # List Products
                    pass
                case 3:
                    # Delete Product
                    pass
                case 4:
                    # Update Product
                    pass
                case 5:
                    # Exit System
                    title("SAINDO DO SISTEMA...")
                    sleep(1)
                    title("ATÉ LOGO!")
                    break

        except Exception as e:
            title("HOUVE UM ERRO AO REALIZAR O PROCEDIMENTO")
            print(e)


if __name__ == "__main__":
    main()