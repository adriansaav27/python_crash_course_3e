from die import Die


# Clase que genera caminos aleatorios.
class RandomWalk:

    # Inicializa los atributos del camino.
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = []
        self.y_values = []

    # Calcula todos los puntos del camino.
    def fill_walk(self, die):

        for roll_num in range(self.num_points):
            self.x_values.append(roll_num)
            self.y_values.append(die.roll())
