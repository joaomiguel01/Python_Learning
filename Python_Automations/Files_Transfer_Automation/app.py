# 1º Forma:

"""from pathlib import Path

arquivos_pdfs = Path("./Arquivos").glob("*.pdf") # Pega caminho dos arquivos PDF
arquivos_mp3 = Path("./Arquivos").glob("*.mp3") # Pega caminho dos arquivos MP3

for arq in arquivos_pdfs:
    # Verifica se é um arquivo
    if arq.is_file():
        arq.rename(f"./Documentos/{arq.name}") # Renomeia a pasta em que está o arquivo
        print(f"Movido: {arq.name}")
    else:
        print(f"Erro ao mover o arquivo {arq.name}!")

for arq in arquivos_mp3:
    # Verifica se é um arquivo
    if arq.is_file():
        arq.rename(f"./Musicas/{arq.name}") # Renomeia a pasta em que está o arquivo
        print(f"Movido: {arq.name}")
    else:
        print(f"Erro ao mover o arquivo {arq.name}!")
"""





# 2º Forma:

"""from glob import glob
from shutil import move
from os import path, makedirs

arquivos_pdfs = glob("./Arquivos/*.pdf")
arquivos_mp3 = glob("./Arquivos/*.mp3")

for arq in arquivos_pdfs:
    destino = "./Documentos"

    makedirs(destino, exist_ok=True)

    if path.isfile(arq):
        move(arq, destino)
        print(f"Movido: {arq}")
    else:
        print(f"Erro ao tentar mover o arquivo: {arq}")

for arq in arquivos_mp3:
    destino = "./Musicas"

    makedirs(destino, exist_ok=True)

    if path.isfile(arq):
        move(arq, destino)
        print(f"Movido: {arq}")
    else:
        print(f"Erro ao tentar mover o arquivo: {arq}")
"""



# 3º Forma:

"""import os

pasta_origem = "./Arquivos"
arquivos = os.listdir(pasta_origem)

for arq in arquivos:

    destino_pdf = "./Documentos/"
    destino_mp3 = "./Musicas/"

    os.makedirs(destino_pdf, exist_ok=True)
    os.makedirs(destino_mp3, exist_ok=True)

    if os.path.isfile(f"{pasta_origem}/{arq}"):
        if arq.endswith(".pdf"):
            os.rename(f"{pasta_origem}/{arq}", f"{destino_pdf}/{arq}")
        elif arq.endswith(".mp3"):
            os.rename(f"{pasta_origem}/{arq}", f"{destino_mp3}/{arq}")
        
        print(f"Movido: {arq}")
"""
