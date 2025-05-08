import pygame
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))  # Agrega la ruta a la raíz
import config

class Ball:
    def __init__(self, x, y, velocity=(0, 0)):
        self.x = x
        self.y = y
        self.radius = config.BALL_RADIUS
        self.color = config.BALL_COLOR
        self.velocity = list(velocity)

    def update(self):
        """Actualiza la posición de la bola."""
        self.x += self.velocity[0]
        self.y += self.velocity[1]

        # Rebote en los bordes
        if self.x - self.radius < 0 or self.x + self.radius > config.SCREEN_WIDTH:
            self.velocity[0] *= -1
        if self.y - self.radius < 0 or self.y + self.radius > config.SCREEN_HEIGHT:
            self.velocity[1] *= -1

    def draw(self, screen):
        """Dibuja la bola en la pantalla."""
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)