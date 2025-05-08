import pygame
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))  # Agrega la ruta a la raíz
import config

class Peg:
    def __init__(self, x, y, color=(0, 0, 255)):  # Azul por defecto
        """Inicializa un peg con posición y color."""
        self.x = x
        self.y = y
        self.radius = 10
        self.color = color
        self.hit_status = False

    def hit(self):
        """Marca el peg como golpeado y cambia su color."""
        self.hit_status = True
        self.color = (100, 100, 100)  # Cambia a gris cuando es golpeado

    def draw(self, screen):
        """Dibuja el peg en pantalla."""
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)