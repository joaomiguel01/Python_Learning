a1 = int(input("Primeiro termo: "))
r = int(input("Razão: "))
term = 1
totalterms = 10
while term <= totalterms:
    print(a1+(term-1)*r, end=" => ")
    term += 1
    if term > totalterms:
        print("Pausa")
        more = int(input("Quer mostrar mais quantos termos?: "))
        totalterms += more
print("FIM!")