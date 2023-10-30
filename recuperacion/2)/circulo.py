
from figura import Figura
import pygame

class Circulo(Figura):
    def dibujar(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), self.punto1, int(abs(self.punto2[0] - self.punto1[0])), 2)