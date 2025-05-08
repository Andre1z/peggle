===========================================
 Peggle Nights Recreation - README
===========================================

🎯 **Descripción**
Este proyecto es una recreación del clásico juego "Peggle Nights" usando Python y Pygame.
Los jugadores pueden lanzar una bola amarilla para impactar pegs en la pantalla y completar niveles.

-------------------------------------------
📌 **Características del juego**
✅ Generación aleatoria de pegs sin que aparezcan sobre la bola.
✅ Relanzamiento automático de la bola cuando cae fuera de la pantalla.
✅ Cambio de color de la bola de azul a amarillo.
✅ Sistema de puntuación que se acumula correctamente.
✅ Reinicio de nivel cuando todos los pegs naranjas han sido impactados.
✅ Interfaz visual fluida con sonidos.

-------------------------------------------
⚙ **Requisitos**
- Python 3.x
- Pygame (`pip install pygame`)
- Archivos de sonido en `assets/sounds/`
- Imágenes en `assets/`

-------------------------------------------
🚀 **Cómo ejecutar el juego**
1️⃣ Clona o descarga el repositorio del proyecto.
2️⃣ Asegúrate de tener Python y Pygame instalados.
3️⃣ Navega al directorio raíz del juego.
4️⃣ Ejecuta el siguiente comando: ```bash python src/game.py```

-------------------------------------------
🛠 **Estructura del proyecto**
- `src/game.py` ➜ Archivo principal para ejecutar el juego.
- `src/board.py` ➜ Maneja la lógica del juego y la puntuación.
- `src/ball.py` ➜ Controla la física y el comportamiento de la bola.
- `src/physics.py` ➜ Aplica colisiones y gravedad a los objetos.
- `src/level_generator.py` ➜ Genera pegs con restricciones de posición.
- `src/config.py` ➜ Contiene todas las configuraciones globales.
- `assets/` ➜ Carpeta que contiene imágenes y sonidos.

-------------------------------------------
🎮 **Controles del juego**
🖱 **Clic izquierdo** ➜ Lanza la bola hacia la dirección indicada.
🖱 **Movimiento del ratón** ➜ Ajusta la dirección antes del lanzamiento.

-------------------------------------------
📌 **Notas adicionales**
Si deseas modificar las reglas del juego, puedes editar `config.py`.
Para cambiar la generación de niveles, ajusta `level_generator.py`.

-------------------------------------------
💡 **Autor**
Este juego ha sido desarrollado como un proyecto de aprendizaje y entretenimiento en Python.

📬 ¿Tienes sugerencias o mejoras? ¡Hazme saber!