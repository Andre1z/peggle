import pygame
from src.peg import Peg

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pegs = []  # Lista para almacenar los pegs
        self.create_pegs()

    def create_pegs(self):
        """Crea pegs en posiciones predefinidas."""
        positions = [(200, 300), (400, 300), (600, 300)]  # Ejemplo de posiciones
        for pos in positions:
            self.pegs.append(Peg(pos[0], pos[1]))

    def update(self):
        """Aquí podríamos actualizar la lógica del tablero en el futuro."""
        pass

    def draw(self, screen):
        """Dibuja los pegs en la pantalla."""
        for peg in self.pegs:
            peg.draw(screen)