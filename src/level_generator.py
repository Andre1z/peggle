import random
import config
from peg import Peg

class LevelGenerator:
    def __init__(self, peg_count=20, orange_ratio=0.25):
        """
        Genera un conjunto de pegs aleatorios con formas variadas.
        - peg_count: Número total de pegs en el nivel.
        - orange_ratio: Porcentaje de pegs que serán naranjas (objetivo).
        """
        self.peg_count = peg_count
        self.orange_ratio = max(orange_ratio, 0.05)  # Asegurar que siempre haya al menos un peg naranja
        self.pegs = self.generate_level()

    def generate_level(self):
        """Genera un nuevo nivel con pegs en posiciones aleatorias y formas variadas."""
        pegs = []
        orange_count = max(int(self.peg_count * self.orange_ratio), 1)  # Garantizar al menos 1 peg naranja

        for _ in range(self.peg_count):
            x = random.randint(50, config.SCREEN_WIDTH - 50)
            y = random.randint(100, config.SCREEN_HEIGHT - 100)

            # Determinar forma del peg: círculo o rectángulo
            shape = random.choice(["circle", "rectangle"])

            # Determinar color (naranja o azul)
            color = (255, 165, 0) if orange_count > 0 else (0, 0, 255)  # Naranja o Azul
            orange_count -= 1 if color == (255, 165, 0) else 0  # Reducir contador de pegs naranjas

            pegs.append(Peg(x, y, shape, color))
        
        return pegs

    def reset_level(self):
        """Regenera el nivel cuando todos los pegs naranjas han sido golpeados."""
        print("🎯 ¡Todos los pegs naranjas han sido golpeados! Generando un nuevo nivel...")
        self.pegs = self.generate_level()