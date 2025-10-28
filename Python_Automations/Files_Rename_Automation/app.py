from os import listdir, path, rename

names = ["João_Marcos",
         "Pedro_Miguel",
         "Mauricio_Junior",
         "Abigail_Freitas",
         "Jilmar_Mendes"]

pasta_origem = "./Arquivos"

arqs = listdir(pasta_origem)

for p, arq in enumerate(arqs):
    if path.isfile(f"{pasta_origem}/{arq}"):
        velho_nome = path.join(pasta_origem, arq)
        novo_nome = f"{pasta_origem}/{p+1}_{names[p]}.txt"
        rename(velho_nome, novo_nome)
        print(f"Arquivo {arq} renomeado com sucesso!")
    else:
        print(f"Erro ao renomear o arquivo {arq}")