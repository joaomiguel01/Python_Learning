velocity = float(input("Digite a velocidade do carro: "))
if velocity > 80:
    print(f"MULTADO!!! Você ultrapassou o limite de 80km/h pague a multa de R${(velocity-80)*7:.2f}")
print("BOM DIA!")