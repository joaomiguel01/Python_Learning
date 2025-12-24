width = float(input("Largura da parede: "))
height = float(input("Altura da parede: "))
area = width*height

print(f"Sua parede de {width}x{height} possui área de {area:.2f}m²")
print(f"Você precisará de {area/2:.2f}L de tinta para pintá-la")
