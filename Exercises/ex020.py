from random import sample
al1 = input("Primeiro aluno: ")
al2 = input("Segundo aluno: ")
al3 = input("Terceiro aluno: ")
al4 = input("Quarto aluno: ")
print(f"Aluno escolhido: {sample([al1, al2, al3, al4], k=4)}")
