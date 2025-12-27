import urllib.request

try:
    urllib.request.urlopen('https://pudim.com.br/')
except:
    print("Não deu")
else:
    print("Acessando site com sucesso")