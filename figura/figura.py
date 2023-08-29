from punto import Punto
from math import pi
class Figura:
    def __init__(self, punto1, punto2):
        self.origen=punto1
        self.fin=punto2
        self.area=0
        self.perimetro=0
    def calcular_area(self):
        pass
    def calcular_perimetro(self):
        pass
    def informar_propiedades(self):
        print("tipo de figura ", str(type(self)).split(".")[1][:-2])
        print("el area es ",self.area)
        print("el perimetro es ", self.perimetro)

class Cuadrado(Figura):
    def calcular_area(self):
        lado=self.origen.calcular_distancia(self.fin)
        self.perimetro=lado*lado
    def calcular_perimetro(self):
        lado=self.origen.calcular_distancia(self.fin)
        self.area=lado*lado
          

