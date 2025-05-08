import pygame
import os
import json

class UI:
    def __init__(self, width, height, sound_manager):
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 36)
        self.reset_button = pygame.Rect(width - 150, height - 50, 140, 40)  # Botón de reinicio
        self.sound_button = pygame.Rect(20, height - 70, 50, 50)  # Botón de configuración de sonido
        self.close_button = pygame.Rect(260, self.height - 280, 30, 30)  # Botón de cerrar configuración
        self.show_sound_settings = False  # Indica si la ventana de configuración está abierta

        # Cargar los volúmenes guardados desde JSON
        self.config_file = os.path.join(os.path.dirname(__file__), "audio_config.json")
        self.music_volume = 1.0
        self.effects_volume = 1.0
        self.load_audio_config(sound_manager)  # Cargar ajustes guardados

        # Cargar imagen de tuerca ⚙️
        self.gear_icon = pygame.image.load("assets/icons/gear.png")
        self.gear_icon = pygame.transform.scale(self.gear_icon, (40, 40))  # Ajustar tamaño

    def load_audio_config(self, sound_manager):
        """Carga los ajustes de audio desde JSON y actualiza las barras de sonido."""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, "r") as file:
                    data = json.load(file)
                    self.music_volume = data.get("music_volume", 1.0)
                    self.effects_volume = data.get("effects_volume", 1.0)
                    sound_manager.set_music_volume(self.music_volume)
                    sound_manager.set_effects_volume(self.effects_volume)
            except json.JSONDecodeError:
                print("⚠ Error: El archivo audio_config.json está vacío o corrupto. Se usarán valores por defecto.")
                self.save_audio_config(sound_manager)
        else:
            self.save_audio_config(sound_manager)

    def save_audio_config(self, sound_manager):
        """Guarda los ajustes de volumen actuales en JSON."""
        data = {
            "music_volume": self.music_volume,
            "effects_volume": self.effects_volume
        }
        with open(self.config_file, "w") as file:
            json.dump(data, file, indent=4)
        
        # Aplicar los cambios al sound_manager
        sound_manager.set_music_volume(self.music_volume)
        sound_manager.set_effects_volume(self.effects_volume)

    def draw(self, screen, score):
        """Dibuja la interfaz en la pantalla."""
        score_text = self.font.render(f"Puntos: {score}", True, (255, 255, 255))
        screen.blit(score_text, (20, 20))

        # Botón de reinicio
        pygame.draw.rect(screen, (200, 50, 50), self.reset_button)
        button_text = self.font.render("Reiniciar", True, (255, 255, 255))
        screen.blit(button_text, (self.width - 140, self.height - 40))

        # Botón de sonido con imagen de tuerca ⚙️
        pygame.draw.circle(screen, (50, 200, 50), (45, self.height - 45), 25)
        screen.blit(self.gear_icon, (25, self.height - 65))  # Ajustar posición

        if self.show_sound_settings:
            self.draw_sound_settings(screen)

    def handle_event(self, event, sound_manager):
        """Detecta si el jugador ha hecho clic en un botón y permite cerrar el menú desde un botón interno."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.show_sound_settings:
                if self.close_button.collidepoint(event.pos):  # Si presiona cerrar, oculta la ventana
                    self.show_sound_settings = False
                    return "sound_settings"
                self.update_volume(event, sound_manager)
                return "sound_settings"
            elif self.sound_button.collidepoint(event.pos):
                self.show_sound_settings = not self.show_sound_settings
                return "sound_settings"
            elif not self.show_sound_settings and self.reset_button.collidepoint(event.pos):
                return "reset"
        return None

    def draw_sound_settings(self, screen):
        """Dibuja la ventana emergente de configuración de sonido con botón para cerrarla."""
        pygame.draw.rect(screen, (50, 50, 50), (20, self.height - 280, 280, 230))
        title = self.font.render("Ajustes de Sonido", True, (255, 255, 255))
        screen.blit(title, (40, self.height - 260))

        # Botón de cierre
        pygame.draw.rect(screen, (200, 50, 50), self.close_button)
        close_text = self.font.render("X", True, (255, 255, 255))
        screen.blit(close_text, (270, self.height - 275))

        music_label = self.font.render("Música", True, (255, 255, 255))
        effects_label = self.font.render("Efectos de Sonido", True, (255, 255, 255))

        screen.blit(music_label, (40, self.height - 230))
        screen.blit(effects_label, (40, self.height - 180))

        # Barras de volumen con indicadores reflejando los valores guardados
        pygame.draw.rect(screen, (100, 100, 100), (40, self.height - 210, 200, 10))  # Música
        pygame.draw.rect(screen, (100, 100, 100), (40, self.height - 160, 200, 10))  # Efectos

        pygame.draw.rect(screen, (255, 255, 255), (40, self.height - 210, int(self.music_volume * 200), 10))
        pygame.draw.rect(screen, (255, 255, 255), (40, self.height - 160, int(self.effects_volume * 200), 10))

    def update_volume(self, event, sound_manager):
        """Ajusta el volumen de la música y los efectos de sonido y guarda los cambios."""
        if self.show_sound_settings and event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 40 <= x <= 240:
                if self.height - 210 <= y <= self.height - 200:  # Control de música
                    self.music_volume = (x - 40) / 200
                    sound_manager.set_music_volume(self.music_volume)
                elif self.height - 160 <= y <= self.height - 150:  # Control de efectos
                    self.effects_volume = (x - 40) / 200
                    sound_manager.set_effects_volume(self.effects_volume)
                self.save_audio_config(sound_manager)  # Guardar cambios en JSON