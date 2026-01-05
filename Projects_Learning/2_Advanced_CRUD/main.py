from gui_utils import menu, read_option, title,read_float, read_int, read_name
from data import add_student, Student, print_data
from time import sleep
import os
import json

def main():
    arq = "database.json"

    if not os.path.exists(arq):
        try:
            title(f"CRIANDO ARQUIVO {arq}")
            with open(arq, "w", encoding="utf-8") as file:
                json.dump([], file, indent=4)
            sleep(1)
        except Exception as e:
            title("ERRO AO TENTAR CRIAR O ARQUIVO")
            print(f"ERRO: {e}")
        finally:
            file.close()

    title(f"ARQUIVO {arq} CARREGADO COM SUCESSO!")
    sleep(1)

    while True:
        try:
            menu("SISTEMA DE CADASTRO DE ALUNOS", 
                 
                 ["Cadastrar Aluno",
                  "Ver Alunos Cadastrados",
                  "Deletar Cadastro", 
                  "Atualizar Cadastro",
                  "Sair Do Programa"])
            
            choice = read_option("Digite sua escolha: ", 5)
            sleep(1)
            print()

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
                    title("LISTA DE ESTUDANTES CADASTRADOS")
                    print(f"{'ID':^5} | {'NOME':<20} | {'IDADE':<3} | {'NOTAS':<20} | {'MÉDIA':<7} | {'DESVIO P.':<7}")
                    print("-"*85)
                    print_data(arq)
                case 3:
                    # Delete Student
                    pass
                case 4:
                    # Update Student
                    pass
                case 5:
                    # Exit Program
                    title("SAINDO DO SISTEMA...")
                    sleep(1)
                    title("ATÉ LOGO!")
                    break
        except Exception as e:
            title("HOUVE UM ERRO AO REALIZAR O PROCEDIMENTO DESEJADO")
            print(f"ERRO: {e}")
            sleep(1)

if __name__ == "__main__":
    main()