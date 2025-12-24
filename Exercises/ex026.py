text = input("Digite algo: ").strip().upper()
print(f"O texto possui {text.count('A')} letras 'A'")
print(f"A primeira letra 'A' está na posição: {text.find('A')+1}")
print(f"A última letra 'A' está na posição: {text.rfind('A')+1}")
