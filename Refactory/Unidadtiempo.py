
class Unidadtiempo:
    def __init__(self, tope):
        # Inicializar la unidad de tiempo con un valor de 0 y un valor máximo especificado (tope)
        self.valor = 0
        self.tope = tope

    def avanzar(self):
        # Avanzar la unidad de tiempo en uno, reiniciar a 0 si alcanza el valor máximo
        if self.valor < self.tope:
            self.valor += 1
        else:
            self.valor = 0

    def resetear(self):
        # Restablecer el valor de la unidad de tiempo a 0
        self.valor = 0

    def getValor(self):
        # Obtener el valor actual de la unidad de tiempo
        return self.valor