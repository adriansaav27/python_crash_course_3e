import pygame
from pygame.sprite import Sprite


# Clase que controla el disparo de los proyectiles de la nave.
class Bullet(Sprite):

    # Crea el objeto del proyectil en la posición de la nave.
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Crea el proyectil en (0, 0) y lo mueve a la posición correcta.
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        self.rect.midtop = ai_game.ship.rect.midtop

        # Guarda la posición del proyectil como un float.
        self.y = float(self.rect.y)

    # Mueve el proyectil.
    def update(self):
        # Actualiza la posición del proyectil.
        self.y -= self.settings.bullet_speed
        # Actualiza la posición del rect.
        self.rect.y = self.y

    # Pinta el proyectil en la pantalla.
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
