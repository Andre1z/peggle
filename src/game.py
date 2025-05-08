import pygame
from board import Board

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Peggle Nights Recreation")

board = Board(WIDTH, HEIGHT)

running = True
clock = pygame.time.Clock()
ball_released = False  # La bola empieza sin moverse
aim_x, aim_y = WIDTH // 2, HEIGHT // 2  # Posición inicial de la mira

while running:
    screen.fill((0, 0, 0))  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION and not ball_released:
            aim_x, aim_y = event.pos  # Actualiza la posición de la mira
        elif event.type == pygame.MOUSEBUTTONDOWN and not ball_released:
            board.ball.velocity = [(aim_x - WIDTH // 2) * 0.05, 5]  # Dirección de la bola basada en la mira
            ball_released = True

    # Dibujar línea de trayectoria antes de disparar
    if not ball_released:
        pygame.draw.line(screen, (255, 255, 255), (WIDTH // 2, 100), (aim_x, aim_y), 2)

    board.update()
    board.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()