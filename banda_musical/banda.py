from instrumento import *
from musico import *
import random

class Banda:
    def __init__(self, nombre_banda):
        self.nombre_banda = nombre_banda
        self.musicos = []

    def agregar_musico(self, musico):
        self.musicos.append(musico)

    def afinar_banda(self):
        print(f"Afinando la {self.nombre_banda}...")
        for musico in self.musicos:
            musico.instrumento.afinar()

    def tocar_banda(self):
        print(f"¡La {self.nombre_banda} está tocando!")
        for musico in self.musicos:
            musico.tocar()

