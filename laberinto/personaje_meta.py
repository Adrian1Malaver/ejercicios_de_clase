import pygame
from configuracion import Configuracion

class PersonajeMeta:
    def __init__(self, x, y, configuracion, color):
        self.rect = pygame.Rect(x * configuracion.CELL_SIZE, y * configuracion.CELL_SIZE,
                                configuracion.CELL_SIZE, configuracion.CELL_SIZE)
        self.color = color

    def dibujar_personaje(self, screen):
        pygame.draw.rect(screen, Configuracion.WHITE, self.rect)
        pygame.draw.circle(screen, self.color, self.rect.center, Configuracion.CELL_SIZE // 2)