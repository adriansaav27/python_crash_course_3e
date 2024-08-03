# Seguimiento de las estadística de Alien Invasion.
class GameStats:

    # Inicializa las estadísticas.
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

    # Inicializa las estadísticas que pueden cambiar durante la partida.
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
