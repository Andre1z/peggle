import random
import config
from peg import Peg

class LevelGenerator:
    def __init__(self, peg_count=20, orange_ratio=0.25):
        """
        Genera un conjunto de pegs aleatorios.
        - peg_count: Número total de pegs en el nivel.
        - orange_ratio: Porcentaje de pegs que serán naranjas (objetivo).
        """
        self.peg_count = peg_count
        self.orange_ratio = orange_ratio
        self.pegs = self.generate_level()

    def generate_level(self):
        """Genera un nuevo nivel con pegs en posiciones aleatorias."""
        pegs = []
        orange_count = int(self.peg_count * self.orange_ratio)  # Número de pegs naranjas

        for _ in range(self.peg_count):
            x = random.randint(50, config.SCREEN_WIDTH - 50)
            y = random.randint(100, config.SCREEN_HEIGHT - 100)

            # Determinar si es naranja o azul
            color = (255, 165, 0) if orange_count > 0 else (0, 0, 255)  # Naranja o Azul
            orange_count -= 1 if color == (255, 165, 0) else 0  # Reducir contador de pegs naranjas

            pegs.append(Peg(x, y, color))
        
        return pegs

    def reset_level(self):
        """Regenera el nivel cuando todos los pegs naranjas han sido golpeados."""
        self.pegs = self.generate_level()