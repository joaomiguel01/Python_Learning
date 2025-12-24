a1 = int(input("Primeiro termo: "))
r = int(input("Razão: "))
term = 1
while term <= 10:
    print(a1+(term-1)*r, end=" => ")
    term += 1
print("FIM!")
