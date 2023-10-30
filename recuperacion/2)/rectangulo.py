
from figura import Figura
import pygame

class Rectangulo(Figura):
    def dibujar(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.punto1[0], self.punto1[1],
                                              abs(self.punto2[0] - self.punto1[0]),
                                              abs(self.punto2[1] - self.punto1[1])), 2)
