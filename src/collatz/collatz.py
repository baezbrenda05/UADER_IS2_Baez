#!/usr/bin/python3
import matplotlib.pyplot as plt

def collatz_iteraciones(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

numeros = list(range(1, 10001))
iteraciones = [collatz_iteraciones(n) for n in numeros]

plt.plot(numeros, iteraciones)
plt.xlabel("Numero n")
plt.ylabel("Iteraciones para converger")
plt.title("Conjetura de Collatz (1 al 10000)")
plt.show()