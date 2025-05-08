import math

def check_collision(ball, peg):
    """Verifica si la bola ha impactado con un peg."""
    distance = math.sqrt((ball.x - peg.x) ** 2 + (ball.y - peg.y) ** 2)
    return distance <= ball.radius + peg.radius

def resolve_collision(ball, peg):
    """Cambia la dirección de la bola dependiendo del ángulo del impacto."""
    if check_collision(ball, peg):
        peg.hit()  # Cambia color del peg

        # Calcular la dirección del impacto con vectores
        impact_x = ball.x - peg.x
        impact_y = ball.y - peg.y
        magnitude = math.sqrt(impact_x**2 + impact_y**2)

        if magnitude > 0:
            normal_x = impact_x / magnitude
            normal_y = impact_y / magnitude

            # Producto escalar para calcular la nueva dirección de rebote
            dot_product = ball.velocity[0] * normal_x + ball.velocity[1] * normal_y
            ball.velocity[0] -= 2 * dot_product * normal_x
            ball.velocity[1] -= 2 * dot_product * normal_y

        # Aumentar velocidad de rebote ligeramente para evitar acumulaciones en un mismo punto
        ball.velocity[0] *= 1.05
        ball.velocity[1] *= 1.05