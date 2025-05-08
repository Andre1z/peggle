import pygame
import json
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))
import config

pygame.mixer.init()

class EfectoSonidos:
    def __init__(self):
        """Carga efectos de sonido y la música, además de restaurar ajustes desde JSON."""
        self.config_file = os.path.join(os.path.dirname(__file__), "audio_config.json")

        self.launch_sound = pygame.mixer.Sound(config.SOUND_LAUNCH)
        self.hit_sound = pygame.mixer.Sound(config.SOUND_HIT)
        self.music_volume = 1.0
        self.effects_volume = 1.0

        # Cargar configuración desde JSON
        self.load_audio_config()

    def load_audio_config(self):
        """Carga los ajustes de audio desde un archivo JSON. Si el archivo está vacío o corrupto, usa valores por defecto."""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, "r") as file:
                    data = json.load(file)
                    self.music_volume = data.get("music_volume", 1.0)
                    self.effects_volume = data.get("effects_volume", 1.0)
            except json.JSONDecodeError:
                print("⚠ Error: El archivo audio_config.json está vacío o corrupto. Se usarán valores por defecto.")
                self.save_audio_config()
        else:
            self.save_audio_config()

        pygame.mixer.music.set_volume(self.music_volume)
        self.launch_sound.set_volume(self.effects_volume)
        self.hit_sound.set_volume(self.effects_volume)

    def save_audio_config(self):
        """Guarda los ajustes de audio en un archivo JSON."""
        data = {
            "music_volume": self.music_volume,
            "effects_volume": self.effects_volume
        }
        with open(self.config_file, "w") as file:
            json.dump(data, file, indent=4)

    def set_music_volume(self, volume):
        """Ajusta el volumen de la música de fondo y guarda la configuración."""
        self.music_volume = volume
        pygame.mixer.music.set_volume(volume)
        self.save_audio_config()

    def set_effects_volume(self, volume):
        """Ajusta el volumen de los efectos y guarda la configuración."""
        self.effects_volume = volume
        self.launch_sound.set_volume(volume)
        self.hit_sound.set_volume(volume)
        self.save_audio_config()

    def play_launch(self):
        """Reproduce el sonido al lanzar la bola con el volumen ajustado."""
        self.launch_sound.set_volume(self.effects_volume)
        self.launch_sound.play()

    def play_hit(self):
        """Reproduce el sonido al golpear un peg con el volumen ajustado."""
        self.hit_sound.set_volume(self.effects_volume)
        self.hit_sound.play()

    def play_background(self):
        """Reproduce música de fondo en bucle."""
        pygame.mixer.music.load(config.SOUND_BACKGROUND)
        pygame.mixer.music.set_volume(self.music_volume)
        pygame.mixer.music.play(-1)  # -1 hace que la música se repita infinitamente