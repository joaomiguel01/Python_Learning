from utils_module_u import menu, read_option, title,read_float, read_int, read_name
from data import add_student, Student, print_data, is_database_exists, grab_data, delete_student, update_student
from time import sleep

def main():
    arq = "database.json"
    is_database_exists(arq)
    sleep(1)

    while True:
        try:
            print()
            menu("SISTEMA DE CADASTRO DE ALUNOS", 
                 
                 ["Cadastrar Aluno",
                  "Ver Alunos Cadastrados",
                  "Deletar Cadastro", 
                  "Atualizar Cadastro",
                  "Sair Do Programa"])
            
            choice = read_option("Digite sua escolha: ", 5)
            sleep(1)

            match choice:
                case 1:
                    # Register Student
                    title("NOVO ALUNO A SER CADASTRADO")
                    id = read_int("ID do Aluno: ")
                    name = read_name("Nome do Aluno: ")
                    birth_year = read_int("Ano de Nascimento: ")
                    note1 = read_float("Nota 1: ")
                    note2 = read_float("Nota 2: ")
                    add_student(arq, Student(id, name, birth_year, [note1, note2]))
                    sleep(1)
                    title("ALUNO CADASTRADO COM SUCESSO!")
                case 2:
                    # List Students
                    print_data(arq)
                case 3:
                    # Delete Student
                    if grab_data(arq):
                        title("PROCEDIMENTO DE DELEÇÃO")
                        sleep(1)
                        print_data(arq)
                        id_deleter = read_int("\nDigite o ID do aluno a ser deletado: ")
                        sleep(1)

                        delete_student(id_deleter, arq)
                    else:
                        raise ValueError("ERROR: database is empty")
                case 4:
                    # Update Student
                    if grab_data(arq):
                        title("PROCEDIMENTO DE ATUALIZAÇÃO")
                        sleep(1)
                        print_data(arq)
                        print()
                        id_updater = read_int("\nDigite o ID do aluno a ser atualizado: ")
                        menu("PROPRIEDADES DO ALUNO PARA ATUALIZAR", ["ID",
                                                                      "NOME",
                                                                      "ANO DE NASCIMENTO",
                                                                      "NOTAS"])
                        op_updater = read_option("\nDigite a opção a ser atualizada: ", 4)

                        update_student(id_updater, op_updater, arq)
                    else:
                        raise ValueError("ERROR: database is empty")
                case 5:
                    # Exit Program
                    title("SAINDO DO SISTEMA...")
                    sleep(1)
                    title("ATÉ LOGO!")
                    break
        except Exception as e:
            title("HOUVE UM ERRO AO REALIZAR O PROCEDIMENTO DESEJADO")
            print(f"{e}")
            sleep(1)

if __name__ == "__main__":
    main()