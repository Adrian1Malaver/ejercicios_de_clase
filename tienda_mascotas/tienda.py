from random import choice
from animales import *
class tienda:
    def __init__(self):
        self.animales=[]
    def agregar_animal(self, animal):
        self.animales.append(animal)
    def entregar_animal(self):
        return choice (self.animales)
