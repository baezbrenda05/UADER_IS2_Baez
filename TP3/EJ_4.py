class Factura:
    def __init__(self, importe):
        self.importe = importe

    def generar(self):
        pass

class FacturaResponsable(Factura):
    def generar(self):
        descuento = self.importe * 0.10
        total = self.importe - descuento
        print(f"Factura A - IVA Responsable - Importe: {self.importe} - Descuento 10%: {descuento} - Total: {total}")

class FacturaNoInscripto(Factura):
    def generar(self):
        descuento = self.importe * 0.05
        total = self.importe - descuento
        print(f"Factura B - IVA No Inscripto - Importe: {self.importe} - Descuento 5%: {descuento} - Total: {total}")

class FacturaExento(Factura):
    def generar(self):
        print(f"Factura C - IVA Exento - Importe: {self.importe} - Sin descuento - Total: {self.importe}")

class FacturaFactory:
    def crear(self, condicion, importe):
        if condicion == "responsable":
            return FacturaResponsable(importe)
        elif condicion == "no_inscripto":
            return FacturaNoInscripto(importe)
        elif condicion == "exento":
            return FacturaExento(importe)
        else:
            print("Condición impositiva no válida")

factory = FacturaFactory()

f1 = factory.crear("responsable", 500000)
f1.generar()

f2 = factory.crear("no_inscripto", 350000)
f2.generar()

f3 = factory.crear("exento", 750000)
f3.generar()