class CalculadorImpuestos:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def calcular(self, base_imponible):
        iva = base_imponible * 0.21
        iibb = base_imponible * 0.05
        contrib_municipal = base_imponible * 0.012
        total = iva + iibb + contrib_municipal
        return total

calc1 = CalculadorImpuestos()
calc2 = CalculadorImpuestos()

print(f"¿Son la misma instancia? {calc1 is calc2}")
print(f"Impuestos sobre 10000: {calc1.calcular(10000)}")
print(f"Impuestos sobre 2500: {calc2.calcular(2500)}")