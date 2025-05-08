import pygame
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))
import config
from board import Board
from ui import UI
from sound import EfectoSonidos

pygame.init()

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("Peggle Nights Recreation")

sound_manager = EfectoSonidos()
ui = UI(config.SCREEN_WIDTH, config.SCREEN_HEIGHT, sound_manager)
board = Board(config.SCREEN_WIDTH, config.SCREEN_HEIGHT)

sound_manager.play_background()
score = 0

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(config.BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        ui_event = ui.handle_event(event, sound_manager)

        if ui.show_sound_settings:
            continue

        if ui_event == "reset":
            board = Board(config.SCREEN_WIDTH, config.SCREEN_HEIGHT)  
            score = 0  

        # Detectar clic para lanzar la bola
        elif event.type == pygame.MOUSEBUTTONDOWN and not board.ball_released:
            board.ball_released = True
            board.ball.released = True
            sound_manager.play_launch()

    board.update()
    board.draw(screen)
    ui.draw(screen, score)  

    pygame.display.flip()
    clock.tick(60)

pygame.quit()