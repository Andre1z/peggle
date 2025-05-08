import pygame

class UI:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 36)
        self.reset_button = pygame.Rect(width - 150, height - 50, 140, 40)  # Botón de reinicio
        self.sound_button = pygame.Rect(20, height - 70, 50, 50)  # Botón circular de sonido (izquierda)
        self.show_sound_settings = False  # Indica si la ventana de configuración está abierta

    def draw(self, screen, score):
        """Dibuja la interfaz en la pantalla."""
        # Marcador de puntos
        score_text = self.font.render(f"Puntos: {score}", True, (255, 255, 255))
        screen.blit(score_text, (20, 20))

        # Botón de reinicio
        pygame.draw.rect(screen, (200, 50, 50), self.reset_button)
        button_text = self.font.render("Reiniciar", True, (255, 255, 255))
        screen.blit(button_text, (self.width - 140, self.height - 40))

        # Botón de sonido (redondo) - Ahora en la izquierda
        pygame.draw.circle(screen, (50, 200, 50), (45, self.height - 45), 25)
        sound_icon = self.font.render("🔊", True, (255, 255, 255))
        screen.blit(sound_icon, (35, self.height - 55))

        # Dibujar ventana de configuración de sonido si está activada
        if self.show_sound_settings:
            self.draw_sound_settings(screen)

    def handle_event(self, event):
        """Detecta si el jugador ha hecho clic en un botón."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.reset_button.collidepoint(event.pos):
                return "reset"
            elif self.sound_button.collidepoint(event.pos):
                self.show_sound_settings = not self.show_sound_settings  # Alterna el menú de sonido
                return "sound_settings"  # Retorna este evento para gestionarlo en game.py
        return None

    def draw_sound_settings(self, screen):
        """Dibuja la ventana emergente de configuración de sonido."""
        pygame.draw.rect(screen, (50, 50, 50), (20, self.height - 250, 280, 200))
        title = self.font.render("Ajustes de Sonido", True, (255, 255, 255))
        screen.blit(title, (40, self.height - 230))

        # Controles de volumen
        music_label = self.font.render("Música", True, (255, 255, 255))
        sound_label = self.font.render("Efectos", True, (255, 255, 255))
        screen.blit(music_label, (40, self.height - 190))
        screen.blit(sound_label, (40, self.height - 140))

        # Deslizadores de volumen
        pygame.draw.rect(screen, (100, 100, 100), (40, self.height - 170, 200, 10))
        pygame.draw.rect(screen, (100, 100, 100), (40, self.height - 120, 200, 10))

    def update_volume(self, event, sound_manager):
        """Permite ajustar el volumen cuando se arrastran los deslizadores."""
        if self.show_sound_settings and event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 40 <= x <= 240:
                if self.height - 170 <= y <= self.height - 160:  # Control de música
                    volume = (x - 40) / 200
                    sound_manager.set_music_volume(volume)
                elif self.height - 120 <= y <= self.height - 110:  # Control de efectos de sonido
                    volume = (x - 40) / 200
                    sound_manager.set_effects_volume(volume)