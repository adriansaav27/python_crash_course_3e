import pygame


# Clase para la gestión de la nave.
class Ship:

    # Inicializa la nave y establece su posición inicial.
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Carga la imagen de la nave.
        self.image = pygame.image.load("./alien_invasion/images/ship.bmp")
        self.rect = self.image.get_rect()

        # Comienza cada nueva nave en la parte inferior central de la pantalla.
        self.rect.midbottom = self.screen_rect.midbottom

        # Guarda el float de la posición exacta de la nave.
        self.x = float(self.rect.x)

        # Bandera de movimiento, comienza con el barco que no está en movimiento.
        self.moving_right = False
        self.moving_left = False

    # Pinta la nave en la posición inicial.
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    # Actualiza la posición del barco según la bandera de movimiento.
    def update(self):
        # Actualiza el valor ´x´ de la nave.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 1
            self.x -= self.settings.ship_speed

        # Actualiza el rect, desde el valor de la x.
        self.rect.x = self.x
