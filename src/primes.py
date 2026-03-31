#!/usr/bin/python3
# Programa: primes.py
# Descripcion: Muestra todos los numeros primos en un intervalo dado
# Autor: Baez Brenda Agustina
# Fecha: 31/03/2026

# Python program to display all the prime numbers within an interval

# Definicion del intervalo de busqueda
lower = 1
upper = 500

# Imprime el encabezado con el rango
print("Prime numbers between", lower, "and", upper, "are:")

# Recorre todos los numeros en el intervalo
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       # Verifica si el numero tiene algun divisor
       for i in range(2, num):
           # Si encuentra un divisor, no es primo
           if (num % i) == 0:
               break
       else:
           # Si no encontro divisores, es primo y lo imprime
           print(num)