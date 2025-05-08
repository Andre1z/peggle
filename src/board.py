import pygame
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))
import config
from peg import Peg
from ball import Ball
import physics
from sound import EfectoSonidos
from particles import Particle  # Importar sistema de partículas

class Board:
    def __init__(self, width, height):
        """Inicializa el tablero y los sonidos."""
        self.width = width
        self.height = height
        self.pegs = []
        self.ball = Ball(config.BALL_INITIAL_POSITION[0], config.BALL_INITIAL_POSITION[1])
        self.sound_manager = EfectoSonidos()
        self.particles = []  # Lista de partículas
        self.create_pegs()

    def create_pegs(self):
        """Crea pegs en posiciones predefinidas."""
        for pos in config.PEG_POSITIONS:
            self.pegs.append(Peg(pos[0], pos[1]))

    def update(self):
        """Actualiza la lógica del tablero."""
        self.ball.update()
        
        # Actualizar partículas
        for p in self.particles:
            p.update()
        self.particles = [p for p in self.particles if p.lifespan > 0]  # Limpiar partículas expiradas

        for peg in self.pegs:
            if physics.check_collision(self.ball, peg):
                physics.resolve_collision(self.ball, peg)
                peg.hit()
                self.sound_manager.play_hit()

                # Generar partículas al impactar un peg
                for _ in range(10):  # Generar múltiples partículas
                    self.particles.append(Particle(peg.x, peg.y, (255, 255, 0)))  # Amarillo

    def draw(self, screen):
        """Dibuja los elementos del tablero en la pantalla."""
        for peg in self.pegs:
            peg.draw(screen)
        self.ball.draw(screen)

        # Dibujar partículas
        for p in self.particles:
            p.draw(screen)