def fatorial(num, show=False):
    fat = 1
    for c in range(num, 0, -1):
        fat *= c
    
    if show == True:
        print(f"{fat}! =", end=" ")
        for c in range(num, 0, -1):
            if c == 1:
                print(f"1 =", end=" ")
            else:
                print(f"{c} X", end=" ")
        print(fat)
    else:
        print(fat)

num = int(input("Digite um número: "))
fatorial(num, show=False)