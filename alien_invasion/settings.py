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
        self.ship_limit = 3

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

        # Que tan rápido se acelera el juego.
        self.speedup_scale = 1.1
        # Qué tan rápido aumentan los valores de puntos de los aliens.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    # Inicializa las configuraciones que cambian a lo largo del juego.
    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0
        # fleet_direction a 1 representa derecha; -1 representa izquierda.
        self.fleet_direction = 1

        # Configuración de la puntuación.
        self.alien_points = 50

    # Incrementa la configuración de las velocidades y los puntos de los aliens.
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
