a1 = int(input("Primeiro termo: "))
r = int(input("Razão: "))

for c in range(a1, a1+10*r, r):
    print(c, end=" => ")
print("FIM")
