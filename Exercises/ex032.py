year = int(input("Digite o ano desejado: "))
if year%4 == 0 and (year%100 != 0 or year%400 == 0):
    print(f"{year} É BISSEXTO")
else:
    print(f"{year} NÃO É BISSEXTO")
