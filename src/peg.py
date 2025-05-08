import pygame
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))  # Agrega la ruta a la raíz
import config

class Peg:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = config.PEG_RADIUS
        self.color = config.PEG_COLOR

    def draw(self, screen):
        """Dibuja el peg en la pantalla."""
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def hit(self):
        """Cambia el color del peg cuando es golpeado."""
        self.color = (255, 255, 0)  # Amarillo para simular impacto