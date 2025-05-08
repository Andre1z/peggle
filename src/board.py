import pygame
import sys
import os

# Ajustar la ruta para importar config.py desde la raíz
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))
import config

from peg import Peg
from ball import Ball
import physics
from sound import SoundManager

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pegs = []
        self.ball = Ball(config.BALL_INITIAL_POSITION[0], config.BALL_INITIAL_POSITION[1])
        self.sound_manager = SoundManager()  # Instancia de sonidos
        self.create_pegs()

    def create_pegs(self):
        """Crea pegs en posiciones predefinidas."""
        for pos in config.PEG_POSITIONS:
            self.pegs.append(Peg(pos[0], pos[1]))

    def update(self):
        """Actualiza la lógica del tablero."""
        self.ball.update()
        
        for peg in self.pegs:
            if physics.check_collision(self.ball, peg):
                physics.resolve_collision(self.ball, peg)
                peg.hit()  # Cambiar color del peg al ser impactado
                self.sound_manager.play_hit()  # Reproduce sonido de impacto

    def draw(self, screen):
        """Dibuja los elementos del tablero en la pantalla."""
        for peg in self.pegs:
            peg.draw(screen)
        self.ball.draw(screen)