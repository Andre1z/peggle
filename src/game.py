import pygame
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))
import config

from board import Board
from ui import UI
from sound import EfectoSonidos  # Importamos la nueva clase con ajustes de volumen persistentes

pygame.init()

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("Peggle Nights Recreation")

sound_manager = EfectoSonidos()  # Inicializar sistema de sonido y cargar volúmenes desde JSON
ui = UI(config.SCREEN_WIDTH, config.SCREEN_HEIGHT, sound_manager)  # Pasar sound_manager a UI
board = Board(config.SCREEN_WIDTH, config.SCREEN_HEIGHT)

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
            pygame.quit()
            sys.exit()

        ui_event = ui.handle_event(event, sound_manager)

        # Permitir ajustes de volumen aunque el menú esté abierto
        if ui.show_sound_settings:
            continue  # Bloquear otros eventos pero permitir ajustes de volumen

        if ui_event == "reset":
            board = Board(config.SCREEN_WIDTH, config.SCREEN_HEIGHT)  
            ball_released = False
            score = 0  
        elif ui_event == "sound_settings":
            pass
        elif event.type == pygame.MOUSEMOTION and not ball_released:
            aim_x, aim_y = event.pos  
        elif event.type == pygame.MOUSEBUTTONDOWN and not ball_released:
            board.ball.velocity = [(aim_x - config.SCREEN_WIDTH // 2) * 0.05, config.BALL_SPEED]
            ball_released = True
            sound_manager.play_launch()

    board.update()
    board.draw(screen)
    ui.draw(screen, score)  

    pygame.display.flip()
    clock.tick(60)

pygame.quit()