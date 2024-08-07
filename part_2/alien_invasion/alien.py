import pygame
from pygame.sprite import Sprite


# Clase que representa un alien.
class Alien(Sprite):

    # Inicializa un alien y lo inserta en una posición inicial.
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Carga la imagen y lo inserta en el atributo rect.
        self.image = pygame.image.load("./alien_invasion/images/alien.bmp")
        self.rect = self.image.get_rect()

        # Inicializa cada alien en la posición de arriba a la izquierda.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Almacena la posición horizontal del alien.
        self.x = float(self.rect.x)

    # Mueve el alien a la izquierda o derecha.
    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    # Devuelve True si el alien está al borde la pantalla.
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
