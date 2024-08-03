# Clase para almacenar todas las configuraciones de Alien Invasion.
class Settings:

    # Inicializa las opciones del juego.
    def __init__(self):
        # Opciones de pantalla.
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (58, 76, 122)

        # Configuración de la nave.
        self.ship_speed = 1.5

        # Configuración de los proyectiles.
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Configuración de los aliens.
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # 1 representa derecha, -1 representa izquierda
        self.fleet_direction = 1
