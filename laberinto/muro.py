import pygame
from configuracion import Configuracion

class Muro:
    def __init__(self, x, y, configuracion):
        self.rect = pygame.Rect(x * configuracion.CELL_SIZE, y * configuracion.CELL_SIZE,
                                configuracion.CELL_SIZE, configuracion.CELL_SIZE)
        self.color = configuracion.BLACK

    def dibujar(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)