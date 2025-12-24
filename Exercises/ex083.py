exp = input("Digite a expressão: ")
stack = []
for char in exp:
    if char == "(":
        stack.append("(")
    elif char == ")":
        if len(stack) > 0:
            stack.pop()
        else:
            stack.append(")")
            break

if len(stack) == 0:
    print("Expressão válida!")
else:
    print("Expressão inválida!")
