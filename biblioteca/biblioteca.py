class Biblioteca:
    def __init__(self):
        self.sedes = {
            "Aduanilla": ["La odisea", "Calculo de Stewart", "Lolita"],
            "Macarena": ["El señor de los anillos", "Romeo y Julieta", "Robin Hood"],
            "La 40": ["Don Quijote de la mancha", "Cien años de soledad", "fisica molecular"],
            "El Vivero": ["Metamorfosis", "Las mil y una noches", "Lupin"]
        }
        self.libros_prestados = []

    def obtener_libros_sede(self, sede):
        return self.sedes.get(sede, [])

    def agregar_libro(self, sede, nombre_libro):
        if sede in self.sedes:
            self.sedes[sede].append(nombre_libro)
            print(f"El libro '{nombre_libro}' se ha agregado a la sede {sede}.")
        else:
            print(f"La sede {sede} no existe.")

    def prestar_libro(self, sede, nombre_libro):
        if sede in self.sedes:
            if nombre_libro in self.sedes[sede]:
                self.sedes[sede].remove(nombre_libro)
                self.libros_prestados.append((sede, nombre_libro))
                print(f"El libro '{nombre_libro}' será prestado en la sede {sede}. Devuélvelo en tres días.")
            else:
                print(f"Lo siento, el libro '{nombre_libro}' no está disponible en la sede {sede}.")
        else:
            print(f"La sede {sede} no existe.")

    def devolver_libro(self, sede, nombre_libro):
        for sede_prestamo, libro_prestado in self.libros_prestados:
            if sede_prestamo == sede and libro_prestado == nombre_libro:
                self.libros_prestados.remove((sede_prestamo, libro_prestado))
                self.sedes[sede].append(nombre_libro)
                print(f"El libro '{nombre_libro}' ha sido devuelto en la sede {sede}.")

    def eliminar_libro(self, sede, nombre_libro):
        if sede in self.sedes:
            if nombre_libro in self.sedes[sede]:
                self.sedes[sede].remove(nombre_libro)
                print(f"El libro '{nombre_libro}' ha sido eliminado de la sede {sede}.")
            else:
                print(f"El libro '{nombre_libro}' no está en la sede {sede}.")

