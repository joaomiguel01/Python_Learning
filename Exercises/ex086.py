mat = [[0, 0, 0], 
       [0, 0, 0],
       [0, 0, 0]]

for r in range(3):
    for c in range(3):
        num = int(input(f"Digite um número na posição [{r}, {c}]: "))
        mat[r][c] = num

for r in range(3):
    for c in range(3):
        print(f"[{mat[r][c]:^5}]", end=" ")
    print()