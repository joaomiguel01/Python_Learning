# Carregar a planilha
# Inserir cada célula da planilha no campo certo
# clicar no botão de cadastrar
import openpyxl
import pyautogui

work_book = openpyxl.load_workbook('vendas_de_produtos.xlsx')
work_page = work_book['vendas']

for linha in work_page.iter_rows(min_row=2):
    pyautogui.click(1296,318, duration=0.5)
    pyautogui.write(linha[0].value)
    pyautogui.click(1297,375, duration=0.5)
    pyautogui.write(linha[1].value)
    pyautogui.click(1302,431, duration=0.5)
    pyautogui.write(str(linha[2].value))
    pyautogui.click(1305,491, duration=0.5)
    pyautogui.write(linha[3].value)

    pyautogui.click(1376,540, duration=0.5)
    pyautogui.click(1388,492, duration=0.5)
