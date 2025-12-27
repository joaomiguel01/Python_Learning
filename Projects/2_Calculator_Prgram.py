# Python Calculator

operator = input("operator (+, -, *, /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1+num2
    print(f"{result:.3f}")
elif operator == "-":
    result = num1-num2
    print(f"{result:.3f}")
elif operator == "*":
    result = num1*num2
    print(f"{result:.3f}")
elif operator == "/":
    result = num1/num2
    print(f"{result:.3f}")
else:
    print(f"{operator} is not a valid operator")