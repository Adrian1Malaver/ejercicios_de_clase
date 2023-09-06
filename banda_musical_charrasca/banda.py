from instrumento import *
from musico import *
from random import randint, choice
class Banda:
    def __init__(self):
        self.instrumentos=[Guitarra(), Maracas(), Charrasca()]
        self.musicos=[]
    def asignar_instrumento(self):
        return choice(self.instrumentos)
    
    def crear_banda(self):
        cant=randint(5,10)
        for i in range(cant):
            self.musicos.append(Musico(self.asignar_instrumento()))
    def afinar_banda(self):
        for m in self.musicos:
            print(m.afinar_instrumento())