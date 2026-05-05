class Componente:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self, nivel=0):
        pass


class Pieza(Componente):
    def mostrar(self, nivel=0):
        print("  " * nivel + f"- Pieza: {self.nombre}")


class Subconjunto(Componente):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.hijos = []

    def agregar(self, componente):
        self.hijos.append(componente)

    def mostrar(self, nivel=0):
        print("  " * nivel + f"[Subconjunto: {self.nombre}]")
        for hijo in self.hijos:
            hijo.mostrar(nivel + 1)


class Ensamblado(Componente):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.subconjuntos = []

    def agregar(self, subconjunto):
        self.subconjuntos.append(subconjunto)

    def mostrar(self, nivel=0):
        print("  " * nivel + f"=== Producto Principal: {self.nombre} ===")
        for sub in self.subconjuntos:
            sub.mostrar(nivel + 1)

producto = Ensamblado("Producto Principal")

for i in range(1, 4):
    sub = Subconjunto(f"Subconjunto {i}")
    for j in range(1, 5):
        sub.agregar(Pieza(f"Pieza {j} (sub{i})"))
    producto.agregar(sub)

producto.mostrar()

print("\n--- Agregando subconjunto opcional ---\n")
sub_opcional = Subconjunto("Subconjunto Opcional")
for j in range(1, 5):
    sub_opcional.agregar(Pieza(f"Pieza {j} (opcional)"))

producto.agregar(sub_opcional)
producto.mostrar()