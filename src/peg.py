import pygame
import random

class Peg:
    def __init__(self, x, y, shape="circle", color=(0, 0, 255)):
        """Inicializa un peg con posición, forma y color."""
        self.x = x
        self.y = y
        self.shape = shape  # Puede ser "circle" o "rectangle"
        self.color = color
        self.hit_status = False

        if self.shape == "circle":
            self.radius = 10
        elif self.shape == "rectangle":
            self.width = 20
            self.height = 10

    def hit(self):
        """Marca el peg como golpeado y cambia su color."""
        self.hit_status = True
        self.color = (100, 100, 100)  # Gris cuando es golpeado

    def draw(self, screen):
        """Dibuja el peg dependiendo de su forma."""
        if self.shape == "circle":
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        elif self.shape == "rectangle":
            pygame.draw.rect(screen, self.color, (self.x - self.width//2, self.y - self.height//2, self.width, self.height))