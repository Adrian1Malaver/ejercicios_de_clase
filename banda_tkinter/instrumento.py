
class Instrumento:
    def __init__(self, nombre):
        self.nombre = nombre

    def afinar(self):
        return "instrumento no afinable" + ", tocando"

class Guitarra(Instrumento):
    def __init__(self):
        super().__init__("Guitarra")

    def afinar(self):
        return "afinando guitarra" + "\ntocando guitarra"

class Maracas(Instrumento):
    def __init__(self):
        super().__init__("Maracas")

    def afinar(self):
        return "no se pueden afinar las maracas" + "\ntocando maracas"

class Charrasca(Instrumento):
    def __init__(self):
        super().__init__("Charrasca")

    def afinar(self):
        return "no se pueden afinar la charrasca" + "\ntocando charrasca"