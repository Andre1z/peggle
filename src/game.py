import pygame
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))
import config
from board import Board
from ui import UI
from sound import EfectoSonidos

pygame.init()

# Cargar imagen de fondo
background_image = pygame.image.load("assets/fondo.webp")

# Aplicar efecto borroso (reduciendo tamaño y expandiéndolo nuevamente)
blurred_image = pygame.transform.smoothscale(background_image, (config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2))
blurred_image = pygame.transform.scale(blurred_image, (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

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
    screen.blit(blurred_image, (0, 0))  

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

        # Actualizar preview de trayectoria cuando el jugador mueve el mouse
        elif event.type == pygame.MOUSEMOTION and not board.ball_released:
            board.aim_x, board.aim_y = event.pos  

        # Detectar clic para lanzar la bola o relanzarla si ha caído
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if board.ball_fallen:  
                board.reset_ball()
            elif not board.ball_released:
                board.release_ball(board.aim_x, board.aim_y)

    board.update()
    score = board.score  # Obtener puntuación actualizada desde Board
    board.draw(screen)
    ui.draw(screen, score)  

    pygame.display.flip()
    clock.tick(60)

pygame.quit()