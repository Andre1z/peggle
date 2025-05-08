import pygame
from board import Board

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Peggle Nights Recreation")

board = Board(WIDTH, HEIGHT)

running = True
clock = pygame.time.Clock()
ball_released = False  # La bola comienza quieta

while running:
    screen.fill((0, 0, 0))  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not ball_released:
            board.ball.velocity = [0, 5]  # Establecemos velocidad en Y
            ball_released = True

    board.update()
    board.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()