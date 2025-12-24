mat = [[0, 0, 0], 
       [0, 0, 0],
       [0, 0, 0]]

sum_even = sum_col3 = bigger_row2 = 0
for r in range(3):
    for c in range(3):
        num = int(input(f"Digite um número na posição [{r}, {c}]: "))
        mat[r][c] = num

        if mat[r][c]%2 == 0:
            sum_even += mat[r][c]
        
        if c == 2:
            sum_col3 += mat[r][c]
        
        if r == 1:
            if c == 0:
                bigger_row2 = mat[r][c]
            else:
                if mat[r][c] > bigger_row2:
                    bigger_row2 = mat[r][c]

for r in range(3):
    for c in range(3):
        print(f"[{mat[r][c]:^5}]", end=" ")
    print()

print("\nSoma dos valores:", sum_even)
print("Soma dos valores da 3º coluna:", sum_col3)
print("Maior valor da 2º linha:", bigger_row2)
