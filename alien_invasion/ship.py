import pygame


# Clase para la gestión de la nave.
class Ship:

    # Inicializa la nave y establece su posición inicial.
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Carga la imagen de la nave.
        self.image = pygame.image.load("./alien_invasion/images/ship.bmp")
        self.rect = self.image.get_rect()

        # Comienza cada nueva nave en la parte inferior central de la pantalla.
        self.rect.midbottom = self.screen_rect.midbottom

    # Pinta la nave en la posición inicial.
    def blitme(self):
        self.screen.blit(self.image, self.rect)
