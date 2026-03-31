#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
# función que calcula el factorial de un número
def factorial(num): 
# si el número es negativo se informa que no existe factorial
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
# si es 0 el factorial es 1
    elif num == 0: 
        return 1
        
    else: 
        fact = 1
# cálculo del factorial usando un ciclo
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

if len(sys.argv) > 1:
    entrada = sys.argv[1]
else:
    entrada = input("Ingrese un numero o rango: ")

# si el usuario ingresa un rango (ej: 4-8, -10, 5-)
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

    for i in range(desde, hasta+1):
        print("Factorial ", i, "! es ", factorial(i))

else:
    num = int(entrada)
    print("Factorial ", num, "! es ", factorial(num))