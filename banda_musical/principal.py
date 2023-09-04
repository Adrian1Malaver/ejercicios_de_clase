from instrumento import *
from musico import *
from banda import *
import random

# Crear instrumentos
instrumentos = [Instrumento("Guitarra"), Instrumento("Batería"), Instrumento("Bajo"), Instrumento("Teclado")]

# Crear músicos con instrumentos aleatorios
banda_musical = Banda("Banda musical")
for i in range(random.randint(3, 6)):
    nombre_musico = f"Músico {i + 1}"
    instrumento_aleatorio = random.choice(instrumentos)
    musico = Musico(nombre_musico, instrumento_aleatorio)
    banda_musical.agregar_musico(musico)

# Afinar e iniciar la actuación
banda_musical.afinar_banda()
banda_musical.tocar_banda()


