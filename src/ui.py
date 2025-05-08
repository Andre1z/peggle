import pygame
import os

class UI:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 36)
        self.reset_button = pygame.Rect(width - 150, height - 50, 140, 40)  # Botón de reinicio
        self.sound_button = pygame.Rect(20, height - 70, 50, 50)  # Botón de configuración de sonido
        self.show_sound_settings = False  # Indica si la ventana de configuración está abierta
        self.music_volume = 1.0
        self.launch_volume = 1.0
        self.hit_volume = 1.0

        # Cargar imagen de tuerca ⚙️
        self.gear_icon = pygame.image.load("assets/icons/gear.png")
        self.gear_icon = pygame.transform.scale(self.gear_icon, (40, 40))  # Ajustar tamaño

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

    def handle_event(self, event):
        """Detecta si el jugador ha hecho clic en un botón."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.reset_button.collidepoint(event.pos):
                return "reset"
            elif self.sound_button.collidepoint(event.pos):
                self.show_sound_settings = not self.show_sound_settings
                return "sound_settings"
        return None

    def draw_sound_settings(self, screen):
        """Dibuja la ventana emergente de configuración de sonido con tres controles ajustables."""
        pygame.draw.rect(screen, (50, 50, 50), (20, self.height - 280, 280, 230))
        title = self.font.render("Ajustes de Sonido", True, (255, 255, 255))
        screen.blit(title, (40, self.height - 260))

        music_label = self.font.render("Música", True, (255, 255, 255))
        launch_label = self.font.render("Lanzamiento", True, (255, 255, 255))
        hit_label = self.font.render("Impacto", True, (255, 255, 255))

        screen.blit(music_label, (40, self.height - 230))
        screen.blit(launch_label, (40, self.height - 180))
        screen.blit(hit_label, (40, self.height - 130))

        # Barras de volumen con indicadores
        pygame.draw.rect(screen, (100, 100, 100), (40, self.height - 210, 200, 10))  # Música
        pygame.draw.rect(screen, (100, 100, 100), (40, self.height - 160, 200, 10))  # Lanzamiento
        pygame.draw.rect(screen, (100, 100, 100), (40, self.height - 110, 200, 10))  # Impacto

        # Indicadores del volumen actual
        pygame.draw.rect(screen, (255, 255, 255), (40, self.height - 210, int(self.music_volume * 200), 10))  # Música
        pygame.draw.rect(screen, (255, 255, 255), (40, self.height - 160, int(self.launch_volume * 200), 10))  # Lanzamiento
        pygame.draw.rect(screen, (255, 255, 255), (40, self.height - 110, int(self.hit_volume * 200), 10))  # Impacto

    def update_volume(self, event, sound_manager):
        """Permite ajustar el volumen de la música y los efectos de sonido de manera independiente."""
        if self.show_sound_settings and event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 40 <= x <= 240:
                if self.height - 210 <= y <= self.height - 200:  # Control de música
                    self.music_volume = (x - 40) / 200
                    sound_manager.set_music_volume(self.music_volume)
                elif self.height - 160 <= y <= self.height - 150:  # Control de lanzamiento
                    self.launch_volume = (x - 40) / 200
                    sound_manager.set_launch_volume(self.launch_volume)
                elif self.height - 110 <= y <= self.height - 100:  # Control de impacto
                    self.hit_volume = (x - 40) / 200
                    sound_manager.set_hit_volume(self.hit_volume)