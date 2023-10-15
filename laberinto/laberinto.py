import pygame
import sys  
from muro import Muro
from camino import Camino
from personaje_meta import PersonajeMeta
from configuracion import Configuracion

class Laberinto:
    def __init__(self, filename, configuracion):
        self.elementos = self.cargar_laberinto(filename)
        self.width = len(self.elementos[0])
        self.height = len(self.elementos)
        self.screen = pygame.display.set_mode((self.width * configuracion.CELL_SIZE, self.height * configuracion.CELL_SIZE))
        pygame.display.set_caption('Laberinto')

        self.configuracion = configuracion

    def cargar_laberinto(self, filename):
        with open(filename, 'r') as file:
            return [list(line.strip()) for line in file]

    def dibujar(self, muros, caminos, personajes_meta):
        for y, fila in enumerate(self.elementos):
            for x, cell in enumerate(fila):
                if cell == '1':
                    muros.append(Muro(x, y, self.configuracion))
                elif cell == '0':
                    caminos.append(Camino(x, y, self.configuracion))
                elif cell == 'X':
                    personajes_meta.append(PersonajeMeta(x, y, self.configuracion, (255, 0, 0)))
                elif cell == 'W':
                    personajes_meta.append(PersonajeMeta(x, y, self.configuracion, (0, 255, 0)))

    def run(self):
        pygame.init()

        clock = pygame.time.Clock()

        muros = []
        caminos = []
        personajes_meta = []

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()  # Esto debería funcionar correctamente ahora

            self.dibujar(muros, caminos, personajes_meta)

            for muro in muros:
                muro.dibujar(self.screen)
            for camino in caminos:
                camino.dibujar(self.screen)
            for personaje_meta in personajes_meta:
                personaje_meta.dibujar_personaje(self.screen)

            pygame.display.flip()
            clock.tick(30)