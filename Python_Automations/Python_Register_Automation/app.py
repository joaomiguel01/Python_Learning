import openpyxl
import pyautogui
from pyperclip import copy
from time import sleep

workbook = openpyxl.load_workbook('produtos_ficticios.xlsx')
page = workbook['Produtos']

# Site para teste de cadstros de produtos
    # https://cadastro-produtos-devaprender.netlify.app/etapa2.html

for l in page.iter_rows(min_row=2):
    # Nome do produto
    pyautogui.click(2309, 363, duration=0.75)
    copy(l[0].value)
    pyautogui.hotkey('ctrl', 'v')

    # Descrição
    pyautogui.click(2295, 455, duration=0.75)
    copy(l[1].value)
    pyautogui.hotkey('ctrl', 'v')

    # Categoria
    pyautogui.click(2288, 575, duration=0.75)
    copy(l[2].value)
    pyautogui.hotkey('ctrl', 'v')

    # Código do Produto
    pyautogui.click(2289, 658, duration=0.75)
    copy(l[3].value)
    pyautogui.hotkey('ctrl', 'v')

    # Peso
    pyautogui.click(2282, 748, duration=0.75)
    copy(l[4].value)
    pyautogui.hotkey('ctrl', 'v')

    # Dimensões
    pyautogui.click(2267, 831, duration=0.75)
    copy(l[5].value)
    pyautogui.hotkey('ctrl', 'v')

    # Próximo - 1
    pyautogui.click(1956, 894, duration=0.75)
    sleep(3)

    # Preço 
    pyautogui.click(2307, 384, duration=0.75)
    copy(l[6].value)
    pyautogui.hotkey('ctrl', 'v')

    # Quantidade
    pyautogui.click(2299, 469, duration=0.75)
    copy(l[7].value)
    pyautogui.hotkey('ctrl', 'v')

    # Data de validade
    pyautogui.click(2287, 545, duration=0.75)
    copy(l[8].value)
    pyautogui.hotkey('ctrl', 'v')

    # Cor
    pyautogui.click(2285, 637, duration=0.75)
    copy(l[9].value)
    pyautogui.hotkey('ctrl', 'v')

    # Tamanho
    pyautogui.click(2272, 723, duration=0.75)
    if l[10].value == "Pequeno":
        pyautogui.click(2242, 760, duration=0.75)
    elif l[10].value == "Médio":
        pyautogui.click(2239, 786, duration=0.75)
    elif l[10].value == "Grande":
        pyautogui.click(2241, 816, duration=0.75)
    
    # Material
    pyautogui.click(2191,795, duration=0.75)
    copy(l[11].value)
    pyautogui.hotkey('ctrl', 'v')

    # Próximo - 2
    pyautogui.click(1958, 874, duration=0.75)
    sleep(3)

    # Fabricante
    pyautogui.click(2283, 401, duration=0.75)
    copy(l[12].value)
    pyautogui.hotkey('ctrl', 'v')

    # País de Origem
    pyautogui.click(2265, 487, duration=0.75)
    copy(l[13].value)
    pyautogui.hotkey('ctrl', 'v')

    # Obs
    pyautogui.click(2258, 575, duration=0.75)
    copy(l[14].value)
    pyautogui.hotkey('ctrl', 'v')

    # Código de barras
    pyautogui.click(2246, 704, duration=0.75)
    copy(l[15].value)
    pyautogui.hotkey('ctrl', 'v')

    # Localização
    pyautogui.click(2232, 796, duration=0.75)
    copy(l[16].value)
    pyautogui.hotkey('ctrl', 'v')

    # Conluir
    pyautogui.click(1952, 859, duration=0.75)
    sleep(1)

    # Ok/Salvar
    pyautogui.click(2727, 614, duration=0.75)
    sleep(2)

    # Adicionar Produto
    pyautogui.click(2577, 642, duration=0.75)
    sleep(2)
