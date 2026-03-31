#!/usr/bin/python3
import sys

class Factorial:
    
    def __init__(self):
        pass
    
    def calcular(self, num):
        if num < 0:
            return 0
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact
    
    def run(self, min, max):
        for i in range(min, max + 1):
            print("Factorial", i, "! es", self.calcular(i))

if len(sys.argv) > 1:
    entrada = sys.argv[1]
else:
    entrada = input("Ingrese un numero o rango: ")

factorial = Factorial()

if "-" in entrada:
    if entrada.startswith("-"):
        desde = 1
        hasta = int(entrada[1:])
    elif entrada.endswith("-"):
        desde = int(entrada[:-1])
        hasta = 60
    else:
        desde, hasta = entrada.split("-")
        desde = int(desde)
        hasta = int(hasta)
    factorial.run(desde, hasta)
else:
    num = int(entrada)
    print("Factorial", num, "! es", factorial.calcular(num))