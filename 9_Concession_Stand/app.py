# Python concession stand program

menu = {"Popcorn":5.99,
        "Pizza":10.99,
        "Fries":2.99,
        "Soda":3.50,
        "Lemonade":4.25}

cart = []
total = 0

print(f"{' MENU ':=^35}")
for key, val in menu.items():
    print(f"{key:.<20}: ${val:>7.2f}")
print("="*35)

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food.capitalize()) is not None:
        cart.append(food)
        total += menu[food.capitalize()]

print(f"{' Your ORDER ':=^35}")
for food in cart:
    print(food, end=" ")

print(f"\nTotal is: ${total:.2f}")