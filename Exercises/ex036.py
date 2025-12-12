r1 = float(input("Digite o valor do primeiro segmento: "))
r2 = float(input("Digite o valor do segundo segmento: "))
r3 = float(input("Digite o valor do terceiro segmento: "))

if r1 < r2+r3 and r2 < r2+r3 and r3 < r1+r2:
    if r1 == r2 == r3:
        rank = "EQUILÁTERO"
    elif r1 != r2 != r3 != r1:
        rank = "ESCALENO"
    else:
        rank = "ISÓSCELES"
    print(f"Esses três segmentos podem formar um triângulo {rank}")
else:
    print("Esses três segmentos não podem formar um triângulo")
