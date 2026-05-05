class TrenLaminador:
    def producir(self, espesor, ancho):
        pass


class TrenCincoMetros(TrenLaminador):
    def producir(self, espesor, ancho):
        print(f"Produciendo en tren de 5 metros (Dimensiones: {espesor} x {ancho})")


class TrenDiezMetros(TrenLaminador):
    def producir(self, espesor, ancho):
        print(f"Produciendo en tren de 10 metros (Dimensiones: {espesor} x {ancho})")


class LaminaAcero:
    def __init__(self, espesor, ancho):
        self.espesor = espesor
        self.ancho = ancho
        self.tren = None

    def seleccionar_tren(self, tren):
        self.tren = tren

    def producir(self):
        if self.tren:
            print("Iniciando producción en tren seleccionado...")
            self.tren.producir(self.espesor, self.ancho)
        else:
            print("No se seleccionó un tren laminador.")


print("=== Fábrica de Láminas de Acero ===")
lamina = LaminaAcero("0.5\"", "1.5m")

lamina.seleccionar_tren(TrenCincoMetros())
lamina.producir()

lamina.seleccionar_tren(TrenDiezMetros())
lamina.producir()