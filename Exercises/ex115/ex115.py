from time import sleep
from dado import leiaInt
from datafile import arquivoExiste, criarArquivo, lerAquivo, cadastrarPessoa
from format import title, colors


def menu():
    title("MENU PRINCIPAL")
    options = [
        "Ver pessoas cadastradas",
        "Cadastrar pessoa",
        "Sair do programa"
    ]

    for pos, o in enumerate(options):
        print(f"{colors['blue']}[{pos+1}]{colors['transparent']} {colors['yellow']}{o}{colors['transparent']}")    
    print("~"*40)


def main():

    arq = "database.txt"

    if not arquivoExiste(arq):
        criarArquivo(arq)

    while True:
        menu()
        option = leiaInt(f"{colors['green']}Sua Opção:{colors['transparent']} ")
        print()
        sleep(1)

        
        if option == 1:
            # Listar pessoas cadastradas
            lerAquivo(arq)
            pass
        elif option == 2:
            # Cadastrar pessoas
            title("NOVO CADASTRO")
            name = input("Nome: ")
            age = leiaInt("Idade: ")
            cadastrarPessoa(arq, name, age)
        elif option == 3:
            title("SAINDO DO PROGRAMA")
            sleep(1)
            break
        else:
            print(f"{colors['red']}ERRO: Digite uma opção válida!{colors['transparent']}")
    
    title("FIM DO PROGRAMA! VOLTE SEMPRE")


if __name__ == "__main__":
    main()
