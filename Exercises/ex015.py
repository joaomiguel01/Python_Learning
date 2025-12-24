days = int(input("Dias alugados: "))
km = float(input("Quilômetros rodados: "))

print(f"Total: R$ {days*60+km*0.15:.2f}")