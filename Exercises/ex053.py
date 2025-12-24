text = input("Digite algo: ").strip().upper().replace(" ", "")
print(f"{text} e {text[::-1]}")
if text == text[::-1]:
    print(f"{text} é um palíndromo")
else:
    print(f"{text} não é um palíndromo")
