from time import sleep
from data import print_data, add_user, User, delete_user, update_user
from gui_utils import menu, read_float, read_int, read_name, read_option, title

def main():
    database = []
    while True:
        try:
            print()
            menu("SISTEMA DE CADASTRO DE USUÁRIOS", options_list=["Cadastrar Usuários",
                                                                  "Ver Usuários",
                                                                  "Deletar Usuários",
                                                                  "Atualizar Usuários",
                                                                  "Sair do Programa"])
            choice = read_option("Digite sua escolha: ", 5)
            sleep(1)
            print()


            if choice == 1:
                # Register Users
                title("NOVO CADASTRO DE USUÁRIO")
                name = read_name("Nome: ")
                year_age = read_int("Ano de Nascimento: ")
                weight = read_float("Peso: ")
                height = read_float("Altura: ")
                add_user(database, User(name, year_age, weight, height))
                title("USUÁRIO CADASTRADO COM SUCESSO!")
                sleep(1)
            elif choice == 2:
                # List Users
                title("LISTA DE CADASTROS DE USUÁRIOS")
                print_data(database)
            elif choice == 3:
                # Delete Users
                delete_user(database)
                title("DELETANDO USUÁRIO...")
                sleep(1)
                title("USUÁRIO DELETADO COM SUCESSO")
            elif choice == 4:
                # Update Users
                update_user(database)
                title("ATUALIZANDO USUÁRIO...")
                sleep(1)
                title("USUÁRIO ATUALIZADO COM SUCESSO")
            elif choice == 5:
                # Exit the program
                title("Saindo do Sistema")
                sleep(1)
                title("Até logo!")
                break
        except Exception as e:
            title("HOUVE ERRO AO REALIZAR O PROCEDIMENTO DESEJADO")
            print(f"ERRO: {e}")
            sleep(1)

if __name__ == "__main__":
    main()