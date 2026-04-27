import math

class CalculadorFactorial:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def calcular(self, n):
        if n < 0:
            print(f"Error: no existe el factorial de números negativos")
            return None
        return math.factorial(n)

calc1 = CalculadorFactorial()
calc2 = CalculadorFactorial()

print(f"¿Son la misma instancia? {calc1 is calc2}")
print(f"Factorial de 12: {calc1.calcular(12)}")
print(f"Factorial de 7: {calc2.calcular(7)}")
print(f"Factorial de 9: {calc1.calcular(9)}")
print(f"Factorial de -3: {calc1.calcular(-3)}")