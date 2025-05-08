import pygame
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))  # Agrega la ruta a la raíz
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

    def update(self):
        """Actualiza la posición de la bola con gravedad y colisiones."""
        if self.released:  # Solo mover la bola si ha sido liberada
            self.velocity[1] += self.gravity  # Aplicar gravedad
            self.x += self.velocity[0]
            self.y += self.velocity[1]

            # Si la bola cae fuera de la pantalla, se reinicia
            if self.y > config.SCREEN_HEIGHT:
                print("⚠ La bola cayó. ¡Lanza otra!")
                self.x = config.BALL_INITIAL_POSITION[0]
                self.y = config.BALL_INITIAL_POSITION[1]
                self.velocity = [0, 0]  # Reiniciar velocidad
                self.released = False  # Resetear para esperar nuevo clic

    def draw(self, screen):
        """Dibuja la bola en la pantalla."""
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)