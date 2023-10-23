from Unidadtiempo import *

class Hora(Unidadtiempo):
    def __init__(self):
        # Inicializar la hora con un valor máximo de 23
        super().__init__(tope=23)

