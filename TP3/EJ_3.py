class Hamburguesa:
    def entregar(self):
        pass

class HamburguesaMostrador(Hamburguesa):
    def entregar(self):
        print("Hamburguesa entregada en mostrador - Tiempo estimado: 5 minutos")

class HamburguesaRetiro(Hamburguesa):
    def entregar(self):
        print("Hamburguesa retirada por el cliente - Tiempo estimado: 10 minutos")

class HamburguesaDelivery(Hamburguesa):
    def entregar(self):
        print("Hamburguesa enviada por delivery - Tiempo estimado: 30 minutos")

class HamburguesaFactory:
    def crear(self, metodo):
        if metodo == "mostrador":
            return HamburguesaMostrador()
        elif metodo == "retiro":
            return HamburguesaRetiro()
        elif metodo == "delivery":
            return HamburguesaDelivery()
        else:
            print("Método de entrega no válido")

factory = HamburguesaFactory()

h1 = factory.crear("mostrador")
h1.entregar()

h2 = factory.crear("retiro")
h2.entregar()

h3 = factory.crear("delivery")
h3.entregar()