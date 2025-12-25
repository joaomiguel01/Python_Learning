from datetime import date
data = dict()
data['nome'] = input("Nome: ")
year_age = int(input("Digite o ano de nascimento: "))
data['idade'] = date.today().year - year_age
data['cpts'] = int(input("Carteira de trabalho (0 caso não tenha): "))

if data['cpts'] > 0:
    data['contratacao'] = int(input("Ano de Contratação: "))
    data['salario'] = float(input("Salário: R$"))
    data['aposentadoria'] = data['idade'] + ((data['contratacao'] + 35) - date.today().year)

print()
for key, val in data.items():
    print(f'{key} tem o valor {val}')
    