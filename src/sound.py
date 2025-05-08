import pygame
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))
import config

pygame.mixer.init()

class SoundManager:
    def __init__(self):
        """Carga los sonidos del juego y almacena los volúmenes de efectos por separado."""
        self.launch_sound = pygame.mixer.Sound(config.SOUND_LAUNCH)
        self.hit_sound = pygame.mixer.Sound(config.SOUND_HIT)
        self.music_volume = 1.0  # Volumen inicial de la música
        self.launch_volume = 1.0  # Volumen inicial del sonido de lanzamiento
        self.hit_volume = 1.0  # Volumen inicial del sonido de impacto

    def play_launch(self):
        """Reproduce el sonido al lanzar la bola con el volumen ajustado."""
        self.launch_sound.set_volume(self.launch_volume)  # Aplica el volumen antes de reproducir
        self.launch_sound.play()

    def play_hit(self):
        """Reproduce el sonido al golpear un peg con el volumen ajustado."""
        self.hit_sound.set_volume(self.hit_volume)  # Aplica el volumen antes de reproducir
        self.hit_sound.play()

    def play_background(self):
        """Reproduce música de fondo en bucle."""
        pygame.mixer.music.load(config.SOUND_BACKGROUND)
        pygame.mixer.music.set_volume(self.music_volume)  # Asegurar volumen antes de reproducir
        pygame.mixer.music.play(-1)  # -1 hace que la música se repita infinitamente

    def set_music_volume(self, volume):
        """Ajusta el volumen de la música de fondo."""
        self.music_volume = volume
        pygame.mixer.music.set_volume(volume)

    def set_launch_volume(self, volume):
        """Ajusta el volumen de lanzar.wav."""
        self.launch_volume = volume
        self.launch_sound.set_volume(volume)

    def set_hit_volume(self, volume):
        """Ajusta el volumen de golpear.wav."""
        self.hit_volume = volume
        self.hit_sound.set_volume(volume)