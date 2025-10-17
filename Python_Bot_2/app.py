# Entrar na planilha
import openpyxl
import pyperclip
import pyautogui
from time import sleep

workbook = openpyxl.load_workbook('produtos_ficticios.xlsx')
sheet_produtos = workbook['Produtos']
# Copiar as informações de um campo
for row in sheet_produtos.iter_rows(min_row=2):

    # Nome do Produto
    nome_produto = row[0].value
    pyperclip.copy(nome_produto)
    pyautogui.click(1946,287, duration=0.5)
    pyautogui.hotkey("ctrl", "v")

    # Descrição do Produto
    descricao = row[1].value
    pyperclip.copy(descricao)
    pyautogui.click(1942,413, duration=0.5)
    pyautogui.hotkey("ctrl", "v")

    # Categoria do Produto
    categoria = row[2].value
    pyperclip.copy(categoria)
    pyautogui.click(1933,572, duration=0.5)
    pyautogui.hotkey("ctrl", "v")

    # Código do Produto
    codigo = row[3].value
    pyperclip.copy(codigo)
    pyautogui.click(1928,686, duration=0.5)
    pyautogui.hotkey("ctrl", "v")

    # Peso do Produto
    peso = row[4].value
    pyperclip.copy(peso)
    pyautogui.click(1942,796, duration=0.5)
    pyautogui.hotkey("ctrl", "v")

    # Dimensões do Produto
    dimensoes = row[5].value
    pyperclip.copy(dimensoes)
    pyautogui.click(1976,905, duration=0.5)
    pyautogui.hotkey("ctrl", "v")

    # Botão Próximo
    pyautogui.click(1771,995, duration=0.5)
    sleep(1)

    # Preço do Produto
    preco = row[6].value
    pyperclip.copy(preco)
    pyautogui.click(1990,321, duration=0.5)
    pyautogui.hotkey("ctrl", "v")

    # Quatidade do Produto
    quantidade = row[7].value
    pyperclip.copy(quantidade)
    pyautogui.click(1972,434, duration=0.5)
    pyautogui.hotkey("ctrl", "v")

    # Data de Validade do Produto
    data_validade = row[8].value
    pyperclip.copy(data_validade)
    pyautogui.click(1924,546, duration=0.5)
    pyautogui.hotkey("ctrl", "v")

    # Cor do Produto
    cor = row[9].value
    pyperclip.copy(cor)
    pyautogui.click(1930,654, duration=0.5)
    pyautogui.hotkey("ctrl", "v")

    # Tamanho do Produto
    tamanho = row[10].value
    pyautogui.click(1885,766, duration=0.5)
    if tamanho == "Pequeno":
        pyautogui.click(1865, 812, duration=0.5)
    elif tamanho == "Médio":
        pyautogui.click(1857, 845, duration=0.5)
    else:
        pyautogui.click(1856, 885, duration=0.5)

    # Material do Produto
    material = row[11].value
    pyperclip.copy(material)
    pyautogui.click(1888,877, duration=0.5)
    pyautogui.hotkey("ctrl", "v")

    # Botão Próximo
    pyautogui.click(1769,961, duration=0.5)
    sleep(1)

    # Fabricante do Produto
    fabricante = row[12].value
    pyperclip.copy(fabricante)
    pyautogui.click(1958,346, duration=0.5)
    pyautogui.hotkey("ctrl", "v")

    # País de Origem do Produto
    pais_origem = row[13].value
    pyperclip.copy(pais_origem)
    pyautogui.click(1947,448, duration=0.5)
    pyautogui.hotkey("ctrl", "v")

    # Observações do Produto
    observacoes = row[14].value
    pyperclip.copy(observacoes)
    pyautogui.click(1936,583, duration=0.5)
    pyautogui.hotkey("ctrl", "v")

    # Código de Barras do Produto
    codigo_barra = row[15].value
    pyperclip.copy(codigo_barra)
    pyautogui.click(1924,733, duration=0.5)
    pyautogui.hotkey("ctrl", "v")

    # Locaização do Produto no Armazém
    localizacao = row[16].value
    pyperclip.copy(localizacao)
    pyautogui.click(1922,851, duration=0.5)
    pyautogui.hotkey("ctrl", "v")

    # Botão de conclusão do Produto
    pyautogui.click(1762,938, duration=0.5)
    sleep(1)

    # Adicionando ao Banco de dados
    pyautogui.click(2736,622, duration=0.5)

    # Adicionando mais um produto
    pyautogui.click(2561,651, duration=0.5)
    sleep(1)