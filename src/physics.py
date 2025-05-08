import math

def check_collision(ball, peg):
    """Verifica si la bola ha impactado con un peg."""
    distance = math.sqrt((ball.x - peg.x) ** 2 + (ball.y - peg.y) ** 2)
    return distance <= ball.radius + peg.radius

def resolve_collision(ball, peg):
    """Cambia la dirección de la bola al impactar con un peg."""
    if check_collision(ball, peg):
        peg.hit()  # Cambia color del peg
        ball.velocity[1] *= -1  # Rebote simple en dirección Y