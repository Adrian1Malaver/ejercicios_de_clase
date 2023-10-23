from Hora import *
from Minuto import *
from Segundo import *

class Cronometro:
    def __init__(self, hora, minuto, segundo):
        # Inicializar los componentes de tiempo
        self.h = hora
        self.m = minuto
        self.s = segundo
        # Inicializar el estado del cronómetro (corriendo o detenido)
        self.parado = False

    def cambiarEstado(self):
        # Alternar el estado del cronómetro
        self.parado = not self.parado

    def avanzar(self):
        # Avanzar el tiempo en un segundo
        self.s.avanzar()
        if self.s.getValor() == 0:
            # KISS: Si los segundos llegan a 0, avanzar los minutos
            self.m.avanzar()
            if self.m.getValor() == 0:
                # KISS: Si los minutos llegan a 0, avanzar las horas
                self.h.avanzar()

    def getTiempo(self):
        # Obtener el tiempo actual en formato HH:MM:SS
        return "{:02d}:{:02d}:{:02d}".format(self.h.getValor(), self.m.getValor(), self.s.getValor())