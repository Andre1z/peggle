import pygame
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))  # Agrega la ruta a la raíz
import config  # Importa config.py correctamente

pygame.mixer.init()  # Inicializa el sistema de audio

class SoundManager:
    def __init__(self):
        self.launch_sound = pygame.mixer.Sound(config.SOUND_LAUNCH)
        self.hit_sound = pygame.mixer.Sound(config.SOUND_HIT)

    def play_launch(self):
        """Reproduce el sonido al lanzar la bola."""
        self.launch_sound.play()

    def play_hit(self):
        """Reproduce el sonido al golpear un peg."""
        self.hit_sound.play()