import pygame
import sys
from laberinto import Laberinto
from configuracion import Configuracion

if __name__ == "__main__":
    # archivo de texto:
    filename = "labyrinth.txt"
    configuracion = Configuracion()
    laberinto_obj = Laberinto(filename, configuracion)
    laberinto_obj.run()