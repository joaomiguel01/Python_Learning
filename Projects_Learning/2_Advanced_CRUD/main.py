from gui_utils import menu, read_option, title
from time import sleep

def main():
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
                    pass
                case 2:
                    # List Students
                    pass
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