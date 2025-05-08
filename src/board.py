import pygame
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))
import config
from peg import Peg
from ball import Ball
import physics
from sound import EfectoSonidos
from level_generator import LevelGenerator  # Importar generación aleatoria de niveles

class Board:
    def __init__(self, width, height):
        """Inicializa el tablero y genera un nivel aleatorio."""
        self.width = width
        self.height = height
        self.level_generator = LevelGenerator()  # Generador de niveles aleatorios
        self.pegs = self.level_generator.pegs  # Cargar pegs generados
        self.ball = Ball(config.BALL_INITIAL_POSITION[0], config.BALL_INITIAL_POSITION[1])
        self.sound_manager = EfectoSonidos()
        self.ball_released = False  # La bola no se mueve hasta que el jugador haga clic

    def update(self):
        """Actualiza la lógica del juego, aplicando gravedad si la bola ha sido lanzada."""
        if self.ball_released:
            physics.apply_gravity(self.ball)  # Aplicar gravedad después del clic
            self.ball.update()
            physics.check_floor_collision(self.ball)  # Verificar si la bola cayó fuera

        # Verificar si todos los pegs naranjas han sido golpeados
        pegs_naranjas_restantes = [peg for peg in self.pegs if peg.color == (255, 165, 0) and not peg.hit_status]

        if not pegs_naranjas_restantes:
            print("🎯 ¡Nivel completado! Generando nuevo nivel...")
            self.level_generator.reset_level()
            self.pegs = self.level_generator.pegs  # Asignar nuevo nivel

        # Colisiones con pegs
        for peg in self.pegs:
            if physics.check_collision(self.ball, peg):
                physics.resolve_collision(self.ball, peg)
                peg.hit()
                self.sound_manager.play_hit()

    def draw(self, screen):
        """Dibuja los elementos del tablero en la pantalla."""
        for peg in self.pegs:
            peg.draw(screen)
        self.ball.draw(screen)