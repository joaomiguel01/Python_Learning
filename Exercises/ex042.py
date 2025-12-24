r1 = float(input("Primeiro segmento de reta: "))
r2 = float(input("Segundo segmento de reta: "))
r3 = float(input("Terceiro segmento de reta: "))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    if r1 == r2 == r3:
        rank = "EQUILÁTERO"
    elif r1 != r2 != r3 != r1:
        rank = "ESCALENO"
    else:
        rank = "ISÓSCELES"
    print(f"Essas três retas podem formar um triângulo {rank}")
else:
    print("Essas três retas não podem formar um triângulo")
    