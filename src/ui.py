import pygame

class UI:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 36)
        self.reset_button = pygame.Rect(width - 150, height - 50, 140, 40)  # Botón de reinicio

    def draw(self, screen, score):
        """Dibuja la interfaz en la pantalla."""
        # Dibujar el marcador
        score_text = self.font.render(f"Puntos: {score}", True, (255, 255, 255))
        screen.blit(score_text, (20, 20))

        # Dibujar botón de reinicio
        pygame.draw.rect(screen, (200, 50, 50), self.reset_button)
        button_text = self.font.render("Reiniciar", True, (255, 255, 255))
        screen.blit(button_text, (self.width - 140, self.height - 40))

    def handle_event(self, event):
        """Detecta si el jugador ha hecho clic en el botón de reinicio."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.reset_button.collidepoint(event.pos):
                return True  # Retorna True si se hace clic en el botón
        return False