def area(x, y):
    return x*y

width = float(input("Largura (m): "))
height = float(input("Altura (m): "))
print(f"Área total: {area(width, height):.2f}m²")
