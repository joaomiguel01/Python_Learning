from utils_module_u import title, menu, read_option, read_name, read_int, read_float
from database import add_customer, Customer, list_customers, delete_customer, print_data, search_customer, update_customer
from time import sleep

def main():
    while True:
        try:
            print()
            menu("SISTEMA DE CADASTRO DE CLIENTES", ["Cadastrar Cliente",
                                                    "Ver Clientes Cadastrados",
                                                    "Deletar Cliente",
                                                    "Atualizar Cliente",
                                                    "Sair do Programa"])
            
            choice = read_option("Digite sua escolha: ", 5)
            print()
            sleep(1)

            match choice:
                case 1:
                    # Register Customer
                    title("NOVO CADASTRO DE CLIENTE")
                    id = read_name("ID do Cliente (3 caracteres): ")
                    name = read_name("Nome do Cliente: ")
                    email = read_name("Email do Cliente: ")
                    birth_year = read_int("Ano de Nascimento: ")
                    total_debt = read_float("Total da Dívida: ")

                    add_customer(Customer(id, name, email, birth_year, total_debt))
                    sleep(1)
                    title("CLIENTE ADICIONADO COM SUCESSO!")
                    sleep(1)
                case 2:
                    # List Customers
                    print_data()
                case 3:
                    # Delete Customer
                    customers = list_customers()
                    if customers:
                        print_data()
                        
                        id_deleter = read_name("\nID do Cliente a ser deletado: ")

                        delete_customer(id_deleter)
                        sleep(1)
                        title("CLIENTE DELETADO COM SUCESSO!")
                        sleep(1)
                case 4:
                    # Update Customer
                    customers = list_customers()
                    if customers:
                        print_data()

                        id_updater = read_name("\nID do Cliente a ser atualizado: ").upper()

                        customer = search_customer(id_updater)
                        sleep(1)

                        menu("PROPRIEDADES QUE PODEM SER ATUALIZADAS", ["Nome do Cliente",
                                                                        "E-mail do Cliente",
                                                                        "Ano de Nascimento",
                                                                        "Dívida do Cliente"])
                        
                        property_updater = read_option("Escolha a propriedade: ", 4)

                        match property_updater:
                            case 1:
                                new_name = read_name("\nNovo nome do Cliente: ")
                                customer.name = new_name
                            case 2:
                                new_email = read_name("\nNovo e-mail do Cliente: ")
                                customer.email = new_email
                            case 3:
                                new_birth_year = read_int("\nAno de nascimento do Cliente: ")
                                customer.birth_year = new_birth_year
                            case 4:
                                new_total_debt = read_float("\nNova dívida do Cliente: ")
                                customer.total_debt = new_total_debt
                        
                        update_customer(customer)
                        sleep(1)
                        title("CLIENTE ATUALIZADO COM SUCESSO!")
                        sleep(1)
                case 5:
                    title("ENCERRANDO PRGRAMA...")
                    sleep(1)
                    title("ATÉ LOGO!")
                    break
        except Exception as e:
            title("HOUVE UM ERRO AO TENTAR REALIZAR O PROCEDIMENTO!")
            print(e)
            sleep(1)
if __name__ == "__main__":
    main()