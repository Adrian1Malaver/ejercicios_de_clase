class Docente:
    def __init__(self, sede, biblioteca):
        self.sede = sede
        self.biblioteca = biblioteca

    def ver_libros_disponibles(self):
        print(f"\nLibros disponibles en la sede {self.sede}:")
        libros_sede = self.biblioteca.obtener_libros_sede(self.sede)
        for libro in libros_sede:
            print(libro)
