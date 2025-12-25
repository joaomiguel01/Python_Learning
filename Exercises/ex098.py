from time import sleep
def contador(start, end, peace):
    print()
    if start <= end:
        for c in range(start, end+1, abs(peace)):
            print(c, end=" => ", flush=True)
            sleep(0.5)
    else:
        for c in range(start, end-1, -abs(peace)):
            print(c, end=" => ", flush=True)
            sleep(0.5)
    
    print("FIM")

contador(1, 10, 1)
contador(10, 0, 2)
start = int(input("Início: "))
end = int(input("Fim: "))
peace = int(input("Passo: "))
contador(start, end, peace)