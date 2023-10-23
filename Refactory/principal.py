
"""Diseñar un programa que contabilize el tiempo por cada segundo como un cronometro
siguiendo el paradigma de la programacion orientada a objetos y con un formato HH:MM:SS al ejecutarse."""


import time
from Cronometro import *

# DRY: Crear instancias de las clases necesarias
hora = Hora()
minuto = Minuto()
segundo = Segundo()
c = Cronometro(hora, minuto, segundo)

cont = 0

# YAGNI: Ejecutar el cronómetro durante 10000 iteraciones
while cont < 10000:
    time.sleep(1)
    c.avanzar()
    print(c.getTiempo())
    cont += 1