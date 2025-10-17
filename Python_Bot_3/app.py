import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui

# Tempo para logar com a conta no web whatsapp
webbrowser.open("https://web.whatsapp.com/")
sleep(30)

# ler informações da planilha
workbook = openpyxl.load_workbook('clientes.xlsx')
clientes = workbook['Sheet1']

for c in clientes.iter_rows(min_row=2):
    # nome, telefone, vencimento
    nome = c[0].value
    telefone = c[1].value
    vencimento = c[2].value
    mensagem = f"Olá {nome} seu boleto vence no dia {vencimento.strftime("%d/%m/%Y")}. Por favor pagar no link https://boletosbons.com"

    # Criar links personalizados e enviar mensagens com base na planilha
    try:
        link_mensagem_whatsapp = f"https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}"
        webbrowser.open(link_mensagem_whatsapp)
        sleep(10)
        pyautogui.click(3473,1038, duration=1)
        pyautogui.click(2904,25, duration=1)
        pyautogui.hotkey("ctrl", "w")
        sleep(5)
    except:
        print(f"Não foi possível enviar mensagem para {nome}")
        with open('erros.csv', 'a', newline='', encoding='utf-8') as arquivo:
            arquivo.write(f"{nome}, {telefone}")