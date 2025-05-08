import pygame
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))  # Agrega la ruta a la raíz
import config  # Ahora puedes importar config.py normalmente


class Ball:
    def __init__(self, x, y, radius=10, color=(0, 0, 255), velocity=(0, 5)):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.velocity = list(velocity)  # Convertimos a lista para modificar valores

    def update(self):
        """Actualiza la posición de la bola según la velocidad."""
        self.x += self.velocity[0]
        self.y += self.velocity[1]

        # Rebote en los bordes de la pantalla
        if self.x - self.radius < 0 or self.x + self.radius > 800:
            self.velocity[0] *= -1  # Invierte dirección en el eje X
        if self.y - self.radius < 0 or self.y + self.radius > 600:
            self.velocity[1] *= -1  # Invierte dirección en el eje Y

    def draw(self, screen):
        """Dibuja la bola en la pantalla."""
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)