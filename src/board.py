import pygame
import sys
import os
import json

sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))
import config
from peg import Peg
from ball import Ball
import physics
from sound import EfectoSonidos
from level_generator import LevelGenerator

class Board:
    def __init__(self, width, height):
        """Inicializa el tablero y carga la puntuación acumulada correctamente."""
        self.width = width
        self.height = height
        self.level_generator = LevelGenerator()
        self.pegs = self.level_generator.pegs
        self.ball = Ball(config.BALL_INITIAL_POSITION[0], config.BALL_INITIAL_POSITION[1])
        self.sound_manager = EfectoSonidos()
        self.ball_released = False  
        self.aim_x = self.ball.x  
        self.aim_y = self.ball.y
        self.score = self.load_score()  

    def load_score(self):
        """Carga la puntuación desde 'src/puntuation.json' si existe."""
        try:
            with open("src/puntuation.json", "r") as file:
                data = json.load(file)
                return data.get("Puntuación", 0)  
        except (FileNotFoundError, json.JSONDecodeError):
            return 0  

    def save_score(self):
        """Guarda la puntuación acumulada correctamente en 'src/puntuation.json'."""
        data = {"Puntuación": self.score}  
        with open("src/puntuation.json", "w") as file:
            json.dump(data, file, indent=4)  

    def release_ball(self, target_x, target_y):
        """Lanza la bola hacia la dirección seleccionada por el jugador."""
        if not self.ball_released:
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
        """Reinicia la bola automáticamente cuando cae fuera de la pantalla."""
        self.ball.x = config.BALL_INITIAL_POSITION[0]
        self.ball.y = config.BALL_INITIAL_POSITION[1]
        self.ball.velocity = [0, 0]
        self.ball_released = False  

    def check_pegs_remaining(self):
        """Verifica si todos los pegs naranjas han sido impactados y recarga el nivel."""
        orange_pegs = [peg for peg in self.pegs if peg.color == (255, 165, 0)]
        if all(peg.hit_status for peg in orange_pegs):  # Si todos han sido impactados
            self.load_new_level()

    def load_new_level(self):
        """Recarga un nuevo nivel cuando todos los pegs naranjas han sido impactados."""
        print("🎯 ¡Nivel completado! Cargando el siguiente nivel...")

        self.level_generator = LevelGenerator()  # Generar nuevo nivel
        self.pegs = self.level_generator.pegs  # Actualizar los pegs
        self.reset_ball()  # Reiniciar bola y permitir nuevo lanzamiento

    def update(self):
        """Actualiza la lógica del juego, aplicando gravedad y verificando colisiones."""
        if self.ball_released:
            physics.apply_gravity(self.ball)  
            self.ball.update()
            physics.check_wall_collision(self.ball)  

            if self.ball.y > self.height:
                self.reset_ball()  

        for peg in self.pegs:
            if physics.check_collision(self.ball, peg):
                physics.resolve_collision(self.ball, peg)
                peg.hit()
                self.sound_manager.play_hit()

                if peg.color == (0, 0, 255):  
                    self.score += 20
                elif peg.color == (255, 165, 0):  
                    self.score += 200

        self.check_pegs_remaining()  # Verificar si todos los pegs naranjas fueron impactados
        self.save_score()  

    def draw(self, screen):
        """Dibuja los elementos del tablero en la pantalla."""
        for peg in self.pegs:
            peg.draw(screen)
        self.ball.draw(screen)

        if not self.ball_released:
            pygame.draw.line(screen, (255, 255, 255), (self.ball.x, self.ball.y), (self.aim_x, self.aim_y), 2)

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Puntuación: {self.score}", True, (255, 255, 255))
        screen.blit(score_text, (20, 20))