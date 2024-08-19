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
            x_direction = choice([1])
            x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            x_step = x_direction * x_distance
            y_direction = choice([1])
            y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            y_step = y_direction * y_distance
            # Rechaza los movimientos que no llevan a ninguna parte.
            if x_step == 0 and y_step == 0:
                continue
            # Calcula la nueva posición.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)
