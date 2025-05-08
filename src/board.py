import pygame
from peg import Peg
from ball import Ball
import physics as physics

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pegs = []
        self.ball = Ball(width // 2, 100)  # Posición inicial de la bola
        self.create_pegs()

    def create_pegs(self):
        """Crea pegs en posiciones predefinidas."""
        positions = [(200, 300), (400, 300), (600, 300)]
        for pos in positions:
            self.pegs.append(Peg(pos[0], pos[1]))

    def update(self):
        """Actualiza la lógica del tablero."""
        self.ball.update()
        
        for peg in self.pegs:
            if physics.check_collision(self.ball, peg):
                physics.resolve_collision(self.ball, peg)

    def draw(self, screen):
        """Dibuja los elementos del tablero en la pantalla."""
        for peg in self.pegs:
            peg.draw(screen)
        self.ball.draw(screen)