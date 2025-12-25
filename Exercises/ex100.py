from random import randint
def function():
    print("Foram sorteados 5 valores:", end=" ")
    nums = []
    total = 0
    for c in range(5):
        num = randint(1, 10)
        nums.append(num)
        if num%2 == 0:
            total += num
        print(num, end=" ")
    print("PRONTO")
    print(f"Somando valores pares de {nums}, temos {total}")

function()