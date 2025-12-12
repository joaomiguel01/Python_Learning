note1 = float(input("Primeira nota: "))
note2 = float(input("Segunda nota: "))
media = (note1+note2)/2

print(f"MÉDIA FINAL: {media:.2f}")
if media < 5:
    print("REPROVADO!")
elif media < 7:
    print("ESTÁ DE RECUPERAÇÃO")
else:
    print("APROVADO!!!")