# Python weight convert program

weight = float(input("Enter you weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {weight:.2f}{unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is: {weight:.2f}{unit}")
else:
    print(f"{unit} was not valid!")
