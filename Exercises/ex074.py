from random import randint
numbers = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

bigger = minor = 0
for pos, n in enumerate(numbers):
    if pos == 0:
        bigger = minor = n
    else:
        if n > bigger:
            bigger = n
        elif n < minor:
            minor = n

print("\nValores:", numbers)
print(f"Maior valor: {bigger}")
print(f"Menor valor: {minor}")
