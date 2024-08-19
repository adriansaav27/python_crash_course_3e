from random import choice


# Clase que genera caminos aleatorios.
class RandomWalk:

    # Inicializa los atributos del camino.
    def __init__(self, num_points=5000):
        self.num_points = num_points

        # Todos los caminos empiezan en el (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    # Calcula todos los puntos del camino.
    def fill_walk(self):
        # Sigue dando pasos hasta la longitud deseada.
        while len(self.x_values) < self.num_points:
            # Decide qué dirección tomar y hasta dónde llegar.
            x_step = self.get_step()
            y_step = self.get_step()

            # Calcula la nueva posición.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance

        # Rechaza los movimientos que no llevan a ninguna parte.
        if step == 0:
            self.get_step()

        return step
