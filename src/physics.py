import math
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))
import config  # Importar configuración global

GRAVITY = 0.2  # Intensidad de la gravedad

def apply_gravity(ball):
    """Aplica gravedad a la bola en cada actualización."""
    ball.velocity[1] += GRAVITY  # Aceleración hacia abajo

def check_collision(ball, peg):
    """Verifica si la bola ha impactado con un peg, considerando su forma."""
    if peg.shape == "circle":
        distance = math.sqrt((ball.x - peg.x) ** 2 + (ball.y - peg.y) ** 2)
        return distance <= ball.radius + peg.radius
    elif peg.shape == "rectangle":
        return (
            peg.x - peg.width//2 <= ball.x <= peg.x + peg.width//2 and
            peg.y - peg.height//2 <= ball.y <= peg.y + peg.height//2
        )

def resolve_collision(ball, peg):
    """Cambia la dirección de la bola dependiendo del impacto."""
    if check_collision(ball, peg):
        peg.hit()  # Cambia color del peg

        if peg.shape == "circle":
            impact_x = ball.x - peg.x
            impact_y = ball.y - peg.y
            magnitude = math.sqrt(impact_x**2 + impact_y**2)

            if magnitude > 0:
                normal_x = impact_x / magnitude
                normal_y = impact_y / magnitude

                dot_product = ball.velocity[0] * normal_x + ball.velocity[1] * normal_y
                ball.velocity[0] -= 2 * dot_product * normal_x
                ball.velocity[1] -= 2 * dot_product * normal_y

            ball.velocity[0] *= 1.05
            ball.velocity[1] *= -0.8  # Rebote con pérdida de energía
        elif peg.shape == "rectangle":
            ball.velocity[1] *= -0.8  # Rebote vertical con pérdida de energía

def check_floor_collision(ball):
    """Verifica si la bola ha caído al suelo y reinicia su posición si es necesario."""
    if ball.y > config.SCREEN_HEIGHT:
        print("⚠ La bola cayó. ¡Lanza otra!")
        ball.x = config.BALL_INITIAL_POSITION[0]
        ball.y = config.BALL_INITIAL_POSITION[1]
        ball.velocity = [0, 0]  # Reiniciar velocidad