# config.py - Configuración global del juego

import os

# Dimensiones de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colores
BACKGROUND_COLOR = (0, 0, 0)  # Negro
PEG_COLOR = (255, 0, 0)  # Rojo
BALL_COLOR = (255, 255, 0)  # Amarillo (antes era azul)
UI_COLOR = (200, 50, 50)  # Rojo oscuro para botones

# Parámetros de la bola
BALL_RADIUS = 10
BALL_INITIAL_POSITION = (SCREEN_WIDTH // 2, 100)
BALL_SPEED = 5

# Parámetros de los pegs
PEG_RADIUS = 20
PEG_POSITIONS = [(200, 300), (400, 300), (600, 300)]  # Posiciones predefinidas

# Rutas de archivos de sonido
BASE_PATH = os.path.abspath(os.path.dirname(__file__))  # Obtiene la ruta absoluta de la raíz

SOUND_LAUNCH = os.path.join(BASE_PATH, "assets/sounds/lanzar.wav")
SOUND_HIT = os.path.join(BASE_PATH, "assets/sounds/golpear.wav")
SOUND_BACKGROUND = os.path.join(BASE_PATH, "assets/sounds/fondo.mp3")