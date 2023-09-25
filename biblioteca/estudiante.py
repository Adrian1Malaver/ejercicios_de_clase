class Estudiante:
    def __init__(self, sede, biblioteca):
        self.sede = sede
        self.codigo = None
        self.biblioteca = biblioteca

    def ingresar_codigo(self, codigo):
        self.codigo = codigo
        print(f"El código {codigo} ha sido registrado en la sede {self.sede}.")

    def pedir_libro(self, nombre_libro):
        if self.codigo is not None:
            print(f"El código {self.codigo} ha pedido el libro '{nombre_libro}' en la sede {self.sede}.")
            self.biblioteca.prestar_libro(self.sede, nombre_libro)
        else:
            print("Debes ingresar un código primero.")

    def devolver_libro(self, nombre_libro):
        if self.codigo is not None:
            print(f"El código {self.codigo} ha devuelto el libro '{nombre_libro}' en la sede {self.sede}.")
            self.biblioteca.devolver_libro(self.sede, nombre_libro)
        else:
            print("Debes ingresar un código primero.")

