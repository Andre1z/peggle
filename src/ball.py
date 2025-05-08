import pygame
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))  
import config

class Ball:
    def __init__(self, x, y, velocity=(0, 0)):
        """Inicializa la bola con posición, color y velocidad."""
        self.x = x
        self.y = y
        self.radius = config.BALL_RADIUS
        self.color = config.BALL_COLOR
        self.velocity = list(velocity)
        self.gravity = 0.3  # Intensidad de la gravedad
        self.released = False  # La bola no se mueve hasta que el jugador haga clic
        self.fallen = False  # Nuevo estado para detectar si la bola ha caído

    def update(self):
        """Actualiza la posición de la bola con gravedad y colisiones."""
        if self.released:  
            self.velocity[1] += self.gravity  
            self.x += self.velocity[0]
            self.y += self.velocity[1]

            # Detectar si la bola ha caído fuera de la pantalla, sin reiniciarla automáticamente
            if self.y > config.SCREEN_HEIGHT:
                print("⚠ La bola ha caído. Haz clic para relanzarla.")
                self.fallen = True  # Marcar como caída para esperar un clic

    def reset(self):
        """Reinicia la bola solo cuando el jugador haga clic."""
        self.x = config.BALL_INITIAL_POSITION[0]
        self.y = config.BALL_INITIAL_POSITION[1]
        self.velocity = [0, 0]
        self.released = False  
        self.fallen = False  # La bola vuelve a estar lista para jugar

    def draw(self, screen):
        """Dibuja la bola en la pantalla."""
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)