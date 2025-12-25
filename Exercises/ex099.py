from time import sleep
def maior(*nums):
    print("Analisando números")
    bigger = 0
    for p, n in enumerate(nums):
        print(n, end=" ", flush=True)
        sleep(0.5)
        if p == 0:
            bigger = n
        else:
            if n > bigger:
                bigger = n

    print(f"Foram informados {len(nums)} números")
    print("Maior valor foi", bigger)

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior()