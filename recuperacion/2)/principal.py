
import pygame
import sys
from circulo import Circulo
from triangulo import Triangulo
from rectangulo import Rectangulo

def main():
    pygame.init()

    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Dibujar Figuras")

    clock = pygame.time.Clock()

    punto1 = (100, 100)  # Punto inicial 
    punto2 = (200, 200)  # Punto final 

    # Modifique el tipo de figura que deseas mostrar, por ejemplo "figura = Circulo(punto1, punto2)"
    figura = Triangulo(punto1, punto2)

    ventana_abierta = True

    while ventana_abierta:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ventana_abierta = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            ventana_abierta = False

        screen.fill((255, 255, 255))
        figura.dibujar(screen)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()