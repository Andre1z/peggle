import pygame
from src.board import Board

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Peggle Nights Recreation")

# Cargar el tablero
board = Board(WIDTH, HEIGHT)

# Bucle principal
running = True
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))  # Fondo negro
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar el tablero
    board.update()
    board.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()