import pygame
from peg import Peg
from ball import Ball
import physics
from particles import Particle

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pegs = []
        self.ball = Ball(width // 2, 100, velocity=(0, 0))
        self.particles = []  # Lista para almacenar partículas
        self.create_pegs()

    def create_pegs(self):
        positions = [(200, 300), (400, 300), (600, 300)]
        for pos in positions:
            self.pegs.append(Peg(pos[0], pos[1]))

    def update(self):
        self.ball.update()
        
        for peg in self.pegs:
            if physics.check_collision(self.ball, peg):
                physics.resolve_collision(self.ball, peg)
                self.create_particles(peg.x, peg.y)  # Generar partículas

        for particle in self.particles:
            particle.update()

        self.particles = [p for p in self.particles if p.lifespan > 0]  # Filtrar partículas activas

    def draw(self, screen):
        for peg in self.pegs:
            peg.draw(screen)
        self.ball.draw(screen)
        for particle in self.particles:
            particle.draw(screen)

    def create_particles(self, x, y):
        """Genera partículas en la posición de impacto."""
        for _ in range(10):
            self.particles.append(Particle(x, y, (255, 255, 0)))