note1 = float(input("Primeira nota: "))
note2 = float(input("Segunda nota: "))
media = (note1+note2)/2

if media < 5:
    rank = "REPROVADO"
elif media < 7:
    rank = "DE RECUPERAÇÃO"
else:
    rank = "APROVADO"

print(f"Média é {media:.2f} e está {rank}")
