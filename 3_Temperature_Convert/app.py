# Python Temperature Convert Program

unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ").upper()
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = temp*9/5+32
    print(f"The temperature in Fahrenheit is: {temp}ºF")
elif unit == "F":
    temp = (temp-32) * 5/9
    print(f"The temperature in Celsius is: {temp}ºC")
else:
    print(f"{unit} is an invalid unit of measurement")