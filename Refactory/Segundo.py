from Unidadtiempo import *

class Segundo(Unidadtiempo):
    def __init__(self):
        # Inicializar el segundo con un valor máximo de 59
        super().__init__(tope=59)