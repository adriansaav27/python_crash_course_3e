import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien


# Clase general para gestionar los activos y el comportamiento del juego.
class AlienInvasion:

    # Inicializa el juego y crea recursos para el juego.
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        # Pantalla completa.
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        # Establece el color de fondo.
        self.screen.fill(self.settings.bg_color)

        # Crea una instancia para almacenar estadísticas.
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # Inicia Alien Invasion con el estado de activo.
        self.game_active = True

    # Inicia el bucle principal del juego.
    def run_game(self):
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

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
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # Pinta la pantalla dibujada más recientemente.
        pygame.display.flip()

    # Crea un nuevo proyectil y lo agrega al grupo.
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    # Actualiza la posición de los proyectiles y borra los proyectiles antiguos.
    def _update_bullets(self):
        self.bullets.update()

        # Borra los proyectiles que desaparecen.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    # Responde a las colisiones proyectil-alien.
    def _check_bullet_alien_collisions(self):

        # Comprueba si algún proyectil colisiona con un alien.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Destruye el proyectil actual y crea una nueva flota.
            self.bullets.empty()
            self._create_fleet()

    # Crea la flota de aliens.
    def _create_fleet(self):
        # Crea un alien y agrega aliens hasta que no quede más espacio.
        # El espacio entre aliens es un alien de ancho y alto.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            # Finaliza la fila, resetea el valor de 'x', e incremente el valor de 'y'.
            current_x = alien_width
            current_y += 2 * alien_height

    # Crea un alien y lo posiciona en la fila.
    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    # Comprueba si la flota está en el borde, después actualiza la posición.
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        # Colisión de alien con la nave.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Busca los aliens que llegan al final de la pantalla.
        self._check_aliens_bottom()

    # Responde adecuadamente si algún alien ha llegado al borde.
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    # Suelta toda la flota y cambia la dirección.
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    # Responde cuando la nave es golpeada.
    def _ship_hit(self):
        if self.stats.ships_left > 0:
            # Decrementa las naves restantes.
            self.stats.ships_left -= 1

            # Elimina las balas y aliens restantes.
            self.bullets.empty()
            self.aliens.empty()

            # Crea una nueva flota y centra la nave.
            self._create_fleet()
            self.ship.center_ship()

            # Pausa.
            sleep(0.5)
        else:
            self.game_active = False

    # Comprueba si hay algún alien ha llegado al final de la pantalla.
    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Se trata de la misma manera como si la nave hubiese sido golpeada.
                self._ship_hit()
                break


# Crea una instancia de juego y ejecuta el juego.
if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
