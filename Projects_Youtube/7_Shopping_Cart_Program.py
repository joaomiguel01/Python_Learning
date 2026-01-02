# Python Shopping Cart Program

foods = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ").lower()
    if food == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        total += price


print("----- YOUR CART -----")
for f in foods:
    print(f, end=" ")
print(f"\nYour total is: ${total:.2f}")
