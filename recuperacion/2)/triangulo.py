
from figura import Figura
import pygame

class Triangulo(Figura):
    def dibujar(self, screen):
        pygame.draw.polygon(screen, (255, 0, 0), [self.punto1, (self.punto1[0], self.punto2[1]), self.punto2], 2)