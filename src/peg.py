import pygame

class Peg:
    def __init__(self, x, y, radius=20, color=(255, 0, 0)):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, screen):
        """Dibuja el peg en la pantalla."""
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def hit(self):
        """Método para cuando la bola golpea el peg. 
        Aquí podríamos cambiar su color o eliminarlo."""
        self.color = (255, 255, 0)  # Cambio de color para simular impacto