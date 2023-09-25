class Administrador:
    def __init__(self, sede, biblioteca):
        self.sede = sede
        self.biblioteca = biblioteca

    def elegir_sede(self, sede):
        self.sede = sede
        print(f"Administrador ahora opera en la sede {self.sede}.")

    def eliminar_libro(self, nombre_libro):
        self.biblioteca.eliminar_libro(self.sede, nombre_libro)

    def agregar_libro(self, nombre_libro):
        self.biblioteca.agregar_libro(self.sede, nombre_libro)
