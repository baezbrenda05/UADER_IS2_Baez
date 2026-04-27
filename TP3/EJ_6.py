import copy

class Notificacion:
    def __init__(self, app, icono, sonido, remitente, mensaje):
        self.app = app
        self.icono = icono
        self.sonido = sonido
        self.remitente = remitente
        self.mensaje = mensaje

    def clone(self):
        return copy.deepcopy(self)

    def mostrar(self):
        print(f"({self.app}) {self.remitente}: {self.mensaje}")

notif_original = Notificacion("WhatsApp", "icono.png", "sonido.mp3", "Juan", "Hola, como estas?")

notif_clon1 = notif_original.clone()
notif_clon1.remitente = "PEDRO"
notif_clon1.mensaje = "¿Recibiste mi correo?"

notif_clon2 = notif_clon1.clone()
notif_clon2.remitente = "CARLOS"
notif_clon2.mensaje = "Que tengas buen dia"

print("=== Mensaje original ===")
notif_original.mostrar()

print("=== Clon 1 ===")
notif_clon1.mostrar()

print("=== Clon 2 (clon del clon) ===")
notif_clon2.mostrar()