class Avion:
    def __init__(self):
        self.partes = []

    def agregar(self, parte):
        self.partes.append(parte)

    def mostrar(self):
        print("Avión construido con:")
        for parte in self.partes:
            print(f"  - {parte}")

class AvionBuilder:
    def __init__(self):
        self.avion = Avion()

    def build_body(self):
        self.avion.agregar("1 Body")

    def build_turbinas(self):
        self.avion.agregar("2 Turbinas")

    def build_alas(self):
        self.avion.agregar("2 Alas")

    def build_tren_aterrizaje(self):
        self.avion.agregar("1 Tren de aterrizaje")

    def get_avion(self):
        return self.avion

class Director:
    def construir(self, builder):
        builder.build_body()
        builder.build_turbinas()
        builder.build_alas()
        builder.build_tren_aterrizaje()

builder = AvionBuilder()
director = Director()
director.construir(builder)
avion = builder.get_avion()
avion.mostrar()