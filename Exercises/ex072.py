numbers = ("ZERO", "UM", "DOIS", "TRÊS", "QUATRO", "QUINTA", "SEIS", "SETE",
           "OITO", "NOVE", "DEZ", "ONZE", "DOZE", "TREZE", "QUATORZE", "QUINZE",
           "DEZESSEIS", "DEZESSETE", "DEZOITO", "DEZENOVE", "VINTE")

num = int(input("Digite um número entre 0 e 20: "))
while not (0 <= num <= 20):
    num = int(input("DADO INVÁLIDO! Digite um número entre 0 e 20: "))

print(f"{num} é {numbers[num]}")
