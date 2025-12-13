# Python Temperature Converter

unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = temp*9/5+32
    print(f"The temperature in Fahrenheit is: {round(temp, 2)}ºF")
elif unit == "F":
    temp = (temp-32)*5/9
    print(f"The temperature in Celsius is: {round(temp, 2)}ºC")
else:
    print(f"{unit} is an invalid unit of measurement")