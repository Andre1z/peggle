import pygame
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))
import config
from peg import Peg
from ball import Ball
import physics
from sound import EfectoSonidos
from level_generator import LevelGenerator

class Board:
    def __init__(self, width, height):
        """Inicializa el tablero y genera un nivel aleatorio."""
        self.width = width
        self.height = height
        self.level_generator = LevelGenerator()
        self.pegs = self.level_generator.pegs
        self.ball = Ball(config.BALL_INITIAL_POSITION[0], config.BALL_INITIAL_POSITION[1])
        self.sound_manager = EfectoSonidos()
        self.ball_released = False  
        self.ball_fallen = False  
        self.aim_x = self.ball.x  
        self.aim_y = self.ball.y
        self.score = 0  # Inicializar puntuación

    def release_ball(self, target_x, target_y):
        """Lanza la bola hacia la dirección seleccionada por el jugador."""
        if not self.ball_released and not self.ball_fallen:
            self.ball_released = True
            self.ball.released = True

            direction_x = target_x - self.ball.x
            direction_y = target_y - self.ball.y
            magnitude = (direction_x**2 + direction_y**2) ** 0.5  

            if magnitude > 0:
                self.ball.velocity[0] = (direction_x / magnitude) * config.BALL_SPEED
                self.ball.velocity[1] = (direction_y / magnitude) * config.BALL_SPEED

            self.sound_manager.play_launch()

    def reset_ball(self):
        """Reinicia la bola y permite al jugador relanzarla manualmente."""
        self.ball.x = config.BALL_INITIAL_POSITION[0]
        self.ball.y = config.BALL_INITIAL_POSITION[1]
        self.ball.velocity = [0, 0]
        self.ball_released = False
        self.ball_fallen = False  

    def update(self):
        """Actualiza la lógica del juego, aplicando gravedad y verificando colisiones."""
        if self.ball_released:
            physics.apply_gravity(self.ball)  
            self.ball.update()
            physics.check_wall_collision(self.ball)  

            # Si la bola cae fuera, permitir relanzarla
            if self.ball.y > self.height:
                self.ball_released = False
                self.ball_fallen = True  
                print("⚠ La bola ha caído. ¡Haz clic para relanzarla!")

        # Verificar colisiones con pegs y sumar puntos
        for peg in self.pegs:
            if physics.check_collision(self.ball, peg):
                physics.resolve_collision(self.ball, peg)
                peg.hit()
                self.sound_manager.play_hit()

                # Sumar puntuación según el color del peg
                if peg.color == (0, 0, 255):  # Azul
                    self.score += 10
                elif peg.color == (255, 165, 0):  # Naranja
                    self.score += 100

    def draw(self, screen):
        """Dibuja los elementos del tablero en la pantalla."""
        for peg in self.pegs:
            peg.draw(screen)
        self.ball.draw(screen)

        # Dibujar línea de trayectoria antes del lanzamiento
        if not self.ball_released and not self.ball_fallen:
            pygame.draw.line(screen, (255, 255, 255), (self.ball.x, self.ball.y), (self.aim_x, self.aim_y), 2)

        # Mostrar puntuación en pantalla
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Puntuación: {self.score}", True, (255, 255, 255))
        screen.blit(score_text, (20, 20))

        # Mostrar mensaje de relanzamiento si la bola ha caído
        if self.ball_fallen:
            text = font.render("¡Haz clic para relanzar la bola!", True, (255, 255, 255))
            screen.blit(text, (self.width // 2 - 150, self.height // 2))