from time import sleep
from utils import menu, title, read_option, read_name, read_int, read_float
from data import print_data, add_user, User


def main():
    database = []
    while True:
        menu()
        
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
            pass
        elif choice == 4:
            # Update Users
            pass
        elif choice == 5:
            # Exit the program
            title("Saindo do Sistema")
            sleep(1)
            title("Até logo!")
            break
        

if __name__ == "__main__":
    main()