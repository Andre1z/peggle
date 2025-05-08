import pygame
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))
import config

pygame.mixer.init()

class EfectoSonidos:
    def __init__(self):
        """Carga ambos efectos de sonido y la música de fondo."""
        self.launch_sound = pygame.mixer.Sound(config.SOUND_LAUNCH)
        self.hit_sound = pygame.mixer.Sound(config.SOUND_HIT)
        self.music_volume = 1.0  # Volumen de la música
        self.effects_volume = 1.0  # Volumen único para efectos

    def play_launch(self):
        """Reproduce el sonido al lanzar la bola con el volumen ajustado."""
        self.launch_sound.set_volume(self.effects_volume)  
        self.launch_sound.play()

    def play_hit(self):
        """Reproduce el sonido al golpear un peg con el volumen ajustado."""
        self.hit_sound.set_volume(self.effects_volume)  
        self.hit_sound.play()

    def set_effects_volume(self, volume):
        """Ajusta el volumen de ambos efectos de sonido al mismo tiempo."""
        self.effects_volume = volume
        self.launch_sound.set_volume(volume)
        self.hit_sound.set_volume(volume)

    def play_background(self):
        """Reproduce música de fondo en bucle."""
        pygame.mixer.music.load(config.SOUND_BACKGROUND)
        pygame.mixer.music.set_volume(self.music_volume)
        pygame.mixer.music.play(-1)  # -1 hace que la música se repita infinitamente

    def set_music_volume(self, volume):
        """Ajusta el volumen de la música de fondo."""
        self.music_volume = volume
        pygame.mixer.music.set_volume(volume)