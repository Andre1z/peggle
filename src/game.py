import pygame
from board import Board
from ui import UI
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))  # Agrega la ruta a la raíz
import config  # Ahora puedes importar config.py normalmente


pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Peggle Nights Recreation")

board = Board(WIDTH, HEIGHT)
ui = UI(WIDTH, HEIGHT)  
score = 0  

running = True
clock = pygame.time.Clock()
ball_released = False  
aim_x, aim_y = WIDTH // 2, HEIGHT // 2  

while running:
    screen.fill((0, 0, 0))  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION and not ball_released:
            aim_x, aim_y = event.pos  
        elif event.type == pygame.MOUSEBUTTONDOWN and not ball_released:
            board.ball.velocity = [(aim_x - WIDTH // 2) * 0.05, 5]  
            ball_released = True
        elif ui.handle_event(event):  
            board = Board(WIDTH, HEIGHT)  
            ball_released = False
            score = 0  

    # Dibujar la trayectoria de la bola antes de disparar
    if not ball_released:
        pygame.draw.line(screen, (255, 255, 255), (WIDTH // 2, 100), (aim_x, aim_y), 2)

    board.update()
    board.draw(screen)
    ui.draw(screen, score)  

    pygame.display.flip()
    clock.tick(60)

pygame.quit()