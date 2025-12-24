from random import randint
data = {}
for c in range(4):
    data[f'jogador{c+1}'] = randint(1, 6)
    print(f"jogador{c+1} tirou {data[f'jogador{c+1}']} no dado")

print()
c = 0
while len(data) != 0:
    c += 1
    for key, val in data.items():
        if val == max(data.values()):
            print(f"{c}º lugar {key} com {val}")
            data.pop(key)
            break