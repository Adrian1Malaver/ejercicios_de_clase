class Instrumento:
    def afinar(self):
        return "instrumento no afinable"+", tocando"
    

class Guitarra(Instrumento):
    def afinar(self):
        return "afinando guitarra"+"\ntocando guitarra"
class Maracas(Instrumento):
    def afinar(self):
        return "no se pueden afinar las maracas"+"\ntocando maracas"
class Charrasca(Instrumento):
    def afinar(self):
        return "no se pueden afinar la charrasca"+"\ntocando charrasca"