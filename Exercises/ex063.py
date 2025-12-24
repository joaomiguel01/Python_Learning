num_terms = int(input("Número de termos a mostrar: "))
n1 = 0
n2 = 1

if num_terms == 1:
    print(n1, end=" => ")
else:
    print(f"{n1} => {n2}", end=" => ")
    c = 3
    while c <= num_terms:
        n3 = n1+n2
        print(n3, end=" => ")
        n1 = n2
        n2 = n3
        c += 1
    
print("FIM!")