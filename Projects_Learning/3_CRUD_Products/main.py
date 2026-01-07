from utils_module_u import title, menu, read_option, read_float, read_int, read_name
from time import sleep
from database import ensure_exists_file, add_product, Product, print_data, delete_product, grab_data, update_product

def main():
    arq = "database.json"
    ensure_exists_file(arq)
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
            print()

            match choice:
                case 1:
                    # Register Product
                    title("NOVO PRODUTO A SER CADASTRADO")
                    code = read_name("Código do Produto (6 caracteres): ")
                    name = read_name("Nome do Produto: ")
                    price = read_float("Preço do Produto: R$")
                    qtd = read_int("Quantidade no estoque: ")
                    add_product(arq, Product(code, name, price, qtd))
                    sleep(1)
                    print()
                    title("PRODUTO CADASTRADO COM SUCESSO!")
                    sleep(1)
                case 2:
                    # List Products
                    print_data(arq)
                case 3:
                    # Delete Product
                    if grab_data(arq):
                        title("PROCEDIMENTO DE DELEÇÃO")
                        sleep(1)
                        print_data(arq)
                        code_deleter = read_name("\nDigite o código do produto a ser deletado: ")
                        delete_product(arq, code_deleter)
                        title("PRODUTO DELETADO COM SUCESSO!")
                    else:
                        raise ValueError("ERROR: The database is empty!")
                case 4:
                    # Update Product
                    if grab_data(arq):
                        title("PROCEDIMENTO DE ATUALIZAÇÃO")
                        sleep(1)
                        print_data(arq)
                        code_updater = read_name("\nDigite o código do produto a ser deletado: ")
                        menu("PROPRIEDADES A SEREM ATUALIZADAS", ["Codígo do Produto",
                                                                  "Nome do Produto",
                                                                  "Preço do Produto",
                                                                  "Quantidade"])
                        op = read_option("Escolha a propriedade desejada: ", 4)
                        match op:
                            case 1:
                                new_value = read_name("\nDigite o novo código do produto (6 caracteres): ")
                            case 2:
                                new_value = read_name("\nDigite o novo nome do produto: ")
                            case 3:
                                new_value = read_float("\nDigite o novo preço do produto: R$")
                            case 4:
                                new_value = read_int("\nDigite a nova quantidade do produto: ")
                        update_product(arq, code_updater, op, new_value)
                        title("PRODUTO ATUALIZADO COM SUCESSO!")
                        sleep(1)
                case 5:
                    # Exit System
                    title("SAINDO DO SISTEMA...")
                    sleep(1)
                    title("ATÉ LOGO!")
                    break
            sleep(1)
        except Exception as e:
            title("HOUVE UM ERRO AO REALIZAR O PROCEDIMENTO")
            print(e)


if __name__ == "__main__":
    main()