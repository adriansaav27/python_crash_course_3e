from random import randint


# Clase qur representa el dado.
class Die:

    # Dado de seis caras.
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    # Devuelve un valor aleatorio entre 1 y el número de lados.
    def roll(self):
        return randint(1, self.num_sides)
