from abc import ABC, abstractmethod

class Mago(ABC):
    @abstractmethod
    def habilidad(self):
        pass

class Guerrero(ABC):
    @abstractmethod
    def habilidad(self):
        pass

class FaccionFactory(ABC):
    @abstractmethod
    def crear_mago(self):
        pass

    @abstractmethod
    def crear_guerrero(self):
        pass

class Lux(Mago):
    def habilidad(self):
        print("Lux lanza un rayo de luz que encadena enemigos")

class Garen(Guerrero):
    def habilidad(self):
        print("Garen gira su espada causando daño masivo")

class Morgana(Mago):
    def habilidad(self):
        print("Morgana lanza cadenas oscuras que inmovilizan al enemigo")

class Darius(Guerrero):
    def habilidad(self):
        print("Darius golpea con su hacha causando sangrado")

class FaccionDemacia(FaccionFactory):
    def crear_mago(self):
        return Lux()

    def crear_guerrero(self):
        return Garen()

class FaccionNoxus(FaccionFactory):
    def crear_mago(self):
        return Morgana()

    def crear_guerrero(self):
        return Darius()

print("=== Facción Demacia ===")
faccion = FaccionDemacia()
faccion.crear_mago().habilidad()
faccion.crear_guerrero().habilidad()

print("=== Facción Noxus ===")
faccion = FaccionNoxus()
faccion.crear_mago().habilidad()
faccion.crear_guerrero().habilidad()