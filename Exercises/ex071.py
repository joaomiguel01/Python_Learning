value = int(input("Digite o valor a ser sacado: R$"))
ced = 50
total_ceds = 0

while True:
    if value >= ced:
        value -= ced
        total_ceds += 1
    else:
        if total_ceds > 0:
            print(f"Total de {total_ceds} cédulas de R${ced}")

        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        
        total_ceds = 0

        if value == 0:
            break