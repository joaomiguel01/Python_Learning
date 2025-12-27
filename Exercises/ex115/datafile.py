from format import title

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        print("Arquivo encontrado com sucesso")
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("Houve um erro na criação do arquivo!")
    else:
        print(f"Arquivo {nome} criado com sucesso")


def lerAquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("Erro ao ler o arquivo!")
    else:
        title("PESSOAS CADASTRADAS")
        for c in a.readlines():
            parts = c.strip().split(';')
            print(f"{parts[0]:.<30} {parts[1]:>3} anos")
    finally:
        a.close()


def cadastrarPessoa(arq, name="desconhecido", age=0):
    try:
        a = open(arq, 'at')
    except:
        print("Houve um ERRO na abertura do arquivo!")
    else:
        try:
            a.write(f"{name};{age}\n")
        except:
            print("Houve um erro na hora de escrever os dados!")
        else:
            print(f"Novo cadastro de {name} adicionado!")
            a.close()
