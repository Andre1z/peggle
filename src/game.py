import pygame
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))
import config
from board import Board
from ui import UI
from sound import EfectoSonidos

pygame.init()

background_image = pygame.image.load("assets/fondo.webp")
blurred_image = pygame.transform.smoothscale(background_image, (config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2))
blurred_image = pygame.transform.scale(blurred_image, (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("Peggle Nights Recreation")

sound_manager = EfectoSonidos()
ui = UI(config.SCREEN_WIDTH, config.SCREEN_HEIGHT, sound_manager)
board = Board(config.SCREEN_WIDTH, config.SCREEN_HEIGHT)  

sound_manager.play_background()

running = True
clock = pygame.time.Clock()

while running:
    screen.blit(blurred_image, (0, 0))  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            board.save_score()  
            pygame.quit()
            sys.exit()

        ui_event = ui.handle_event(event, sound_manager)
        if ui.show_sound_settings:
            continue

        if ui_event == "reset":
            board = Board(config.SCREEN_WIDTH, config.SCREEN_HEIGHT)  

        elif event.type == pygame.MOUSEMOTION and not board.ball_released:
            board.aim_x, board.aim_y = event.pos  

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not board.ball_released:
                board.release_ball(board.aim_x, board.aim_y)

    board.update()
    board.draw(screen)
    
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Puntuación: {board.score}", True, (255, 255, 255))
    screen.blit(score_text, (20, 20))

    ui.draw(screen, board.score)  

    pygame.display.flip()
    clock.tick(60)

pygame.quit()