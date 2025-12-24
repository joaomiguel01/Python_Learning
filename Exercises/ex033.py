num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))
num3 = int(input("Terceiro valor: "))

bigger = num1
if num2 > num1 and num2 > num3:
    bigger = num2
elif num3 < num1 and num3 > num2:
    bigger = num3

minor = num1
if num2 < num1 and num2 < num3:
    minor = num2
elif num3 < num1 and num3 < num2:
    minor = num3

print("Maior valor digitado:", bigger)
print("Menor valor digitado:", minor)
