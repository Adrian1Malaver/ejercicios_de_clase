from Unidadtiempo import *

class Minuto(Unidadtiempo):
    def __init__(self):
        # Inicializar el minuto con un valor máximo de 59
        super().__init__(tope=59)
