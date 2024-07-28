import sys
import pygame
from settings import Settings
from ship import Ship


# Clase general para gestionar los activos y el comportamiento del juego.
class AlienInvasion:

    # Inicializa el juego y crea recursos para el juego.
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        # Establece el color de fondo.
        self.screen.fill(self.settings.bg_color)

        self.ship = Ship(self)

    # Inicia el bucle principal del juego.
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    # Mira los eventos del teclado y ratón.
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    # Responde al pulsar las teclas.
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

    # Responde al dejar de pulsar las teclas.
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_q:
            sys.exit()

    # Vuelva a dibujar la pantalla durante cada paso por el bucle.
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Pinta la pantalla dibujada más recientemente.
        pygame.display.flip()


# Crea una instancia de juego y ejecuta el juego.
if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
