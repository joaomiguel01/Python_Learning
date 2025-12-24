weight = float(input("Digite sua massa (kg): "))
height = float(input("Digite sua altura (m): "))
imc = weight/height**2

if imc < 18.5:
    rank = "ABAIXO DO PESO"
elif imc < 25:
    rank = "NO PESO IDEAL"
elif imc < 30:
    rank = "COM SOBREPESO"
elif imc <= 40:
    rank = "EM OBESIDADE"
else:
    rank = "EM OBESIDADE MÓRBIDA"

print(f"Seu IMC é {imc:.2f} e você está {rank}")