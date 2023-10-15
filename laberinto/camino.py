import pygame
from configuracion import Configuracion

class Camino:
    def __init__(self, x, y, configuracion):
        self.rect = pygame.Rect(x * configuracion.CELL_SIZE, y * configuracion.CELL_SIZE,
                                configuracion.CELL_SIZE, configuracion.CELL_SIZE)
        self.color = configuracion.WHITE

    def dibujar(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)