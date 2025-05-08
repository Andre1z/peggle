import pygame
import random

class Particle:
    def __init__(self, x, y, color, lifespan=30):
        """Inicializa una partícula con posición, color y duración."""
        self.x = x
        self.y = y
        self.color = color
        self.lifespan = lifespan
        self.velocity = [random.uniform(-2, 2), random.uniform(-2, 2)]

    def update(self):
        """Reduce la vida de la partícula y mueve su posición."""
        self.lifespan -= 1
        self.x += self.velocity[0]
        self.y += self.velocity[1]

    def draw(self, screen):
        """Dibuja la partícula en la pantalla."""
        if self.lifespan > 0:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 3)