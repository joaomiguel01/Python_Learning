bigger = minor = 0
for c in range(1, 6):
    weight = float(input(f"Peso da {c}º pessoa: "))

    if c == 1:
        bigger = minor = weight
    else:
        if weight > bigger:
            bigger = weight
        elif weight < minor:
            minor = weight

print(f"\nMaior peso: {bigger:.2f}kg")
print(f"Menor peso: {minor:.2f}kg")
