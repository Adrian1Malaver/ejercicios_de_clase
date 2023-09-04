from instrumento import *

class Musico:
    def __init__(self, nombre, instrumento):
        self.nombre = nombre
        self.instrumento = instrumento

    def tocar(self):
        print(f"{self.nombre} tocando {self.instrumento.nombre}")

