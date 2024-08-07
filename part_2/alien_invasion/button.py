import pygame.font


# Clase para contruir los botones del juego.
class Button:

    def __init__(self, ai_game, msg):
        # Inicializa los atributos del botón.
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Inicializa las dimensiones y propiedades del botón.
        self.width, self.height = 200, 50
        self.button_color = (156, 156, 156)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Contruye el rect del objeto y los centra.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # El botón del mensaje necesita ser preparado.
        self._prep_msg(msg)

    # Renderiza el botón y centra el texto en el botoón.
    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    # Pinta un botoón y dibuja el mensaje.
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
