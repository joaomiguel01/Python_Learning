from random import randint
from time import sleep
num_sorts = int(input("Quantos jogos a sortear: "))
numbers = []
for sort in range(num_sorts):
    for c in range(6):
        num = randint(1, 60)
        while num in numbers:
            num = randint(1, 60)
        
        numbers.append(num)
    print(f"Jogo {sort+1}:", numbers)
    sleep(1)
    numbers.clear()