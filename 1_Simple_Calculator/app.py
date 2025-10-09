# Python Calculator

operation = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the first number: "))

if operation == "+":
    result = num1+num2
    print(round(result, 3))
elif operation == "-":
    result = num1+-num2
    print(round(result, 3))
elif operation == "*":
    result = num1*num2
    print(round(result, 3))
elif operation == "/":
    result = num1/num2
    print(round(result, 3))
else:
    print(f"{operation} is not a valid operator!")
