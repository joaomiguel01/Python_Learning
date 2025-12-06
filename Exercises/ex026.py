year = int(input("Digite o ano: "))
if year%4 == 0 and (year%100 != 0 or year%400 == 0):
    print(f"{year} é BISSEXTO!")
else:
    print(f"{year} não é BISSEXTO!")
