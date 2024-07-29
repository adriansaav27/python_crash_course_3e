# Clase para almacenar todas las configuraciones de Alien Invasion.
class Settings:

    # Inicializa las opciones del juego.
    def __init__(self):
        # Opciones de pantalla.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (58, 76, 122)

        # Configuración de la nave.
        self.ship_speed = 1.5

        # Configuración de los proyectiles.
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
