import pygame
from board import Board  # Asegúrate de que el import sea correcto

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Peggle Nights Recreation")

# Cargar el tablero
board = Board(WIDTH, HEIGHT)

# Variables de control
running = True
clock = pygame.time.Clock()
ball_released = False  # La bola empieza sin moverse

while running:
    screen.fill((0, 0, 0))  # Fondo negro

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not ball_released:
            board.ball.velocity = [0, 5]  # La bola cae cuando el jugador hace clic
            ball_released = True

    # Actualizar la lógica del juego
    board.update()
    board.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()