temp = float(input("Enter the temperature: "))
unit = input("Is this the temperature in Celsius or Fahrenheit (C/F): ")

if unit == "C":
    temp = temp*9/5+32
    print(f"The temperature in Fahrenheit is: {temp:.2f}ºF")
elif unit == "F":
    temp = (temp-32) * 5 / 9
    print(f"The temperature in Celsius is: {temp:.2f}ºC")
else:
    print(f"{unit} is an invalid unit of measurement")