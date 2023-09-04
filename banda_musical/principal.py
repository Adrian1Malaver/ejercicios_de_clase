from instrumento import *
from musico import *
from banda import *
import random

# Crear al menos 5 instrumentos
instrumentos = [
    Instrumento("Guitarra"),
    Instrumento("Batería"),
    Instrumento("Bajo"),
    Instrumento("Teclado"),
    Instrumento("Violín"),
]

# Crear músicos con instrumentos aleatorios
banda_musical = Banda("Banda")
numero_musicos = random.randint(3, 10)  # Entre 3 y 10 músicos
for i in range(numero_musicos):
    nombre_musico = f"Músico {i + 1}"
    instrumento_aleatorio = random.choice(instrumentos)
    musico = Musico(nombre_musico, instrumento_aleatorio)
    banda_musical.agregar_musico(musico)

# Afinar y tocar
banda_musical.afinar_banda()
banda_musical.tocar_banda()


