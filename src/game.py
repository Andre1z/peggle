import pygame
import sys
import os

# Ajustar la ruta para importar config.py desde la raíz del proyecto
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))
import config

from board import Board
from ui import UI
from sound import SoundManager

pygame.init()

# Configuración de pantalla
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("Peggle Nights Recreation")

# Inicializar elementos del juego
board = Board(config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
ui = UI(config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
sound_manager = SoundManager()
sound_manager.play_background()  # Reproducir música de fondo
score = 0  

running = True
clock = pygame.time.Clock()
ball_released = False  
aim_x, aim_y = config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2  

while running:
    screen.fill(config.BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION and not ball_released:
            aim_x, aim_y = event.pos  
        elif event.type == pygame.MOUSEBUTTONDOWN and not ball_released:
            board.ball.velocity = [(aim_x - config.SCREEN_WIDTH // 2) * 0.05, config.BALL_SPEED]
            ball_released = True
            sound_manager.play_launch()
    
    # Manejo de eventos de UI
    ui_event = ui.handle_event(event)
    if ui_event == "reset":
        board = Board(config.SCREEN_WIDTH, config.SCREEN_HEIGHT)  
        ball_released = False
        score = 0  
    elif ui_event == "sound_settings":
        pass  # La visibilidad del menú ya se gestiona en UI.py
    elif ui.show_sound_settings:
        ui.update_volume(event, sound_manager)  # Ajuste de volumen cuando la ventana está abierta

    board.update()
    board.draw(screen)
    ui.draw(screen, score)  

    pygame.display.flip()
    clock.tick(60)

pygame.quit()