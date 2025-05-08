import pygame
import sys
import os

# Ajustar la ruta para importar config.py desde la raíz
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))
import config

pygame.mixer.init()

class SoundManager:
    def __init__(self):
        """Carga los sonidos del juego desde config.py"""
        self.launch_sound = pygame.mixer.Sound(config.SOUND_LAUNCH)
        self.hit_sound = pygame.mixer.Sound(config.SOUND_HIT)

    def play_launch(self):
        """Reproduce el sonido al lanzar la bola."""
        self.launch_sound.play()

    def play_hit(self):
        """Reproduce el sonido al golpear un peg."""
        self.hit_sound.play()

    def play_background(self):
        """Reproduce música de fondo en bucle."""
        pygame.mixer.music.load(config.SOUND_BACKGROUND)
        pygame.mixer.music.play(-1)  # -1 hace que la música se repita infinitamente