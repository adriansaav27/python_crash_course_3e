import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Sigue haciendo nuevos caminos, mientras el programa esté activo.

while True:

    # Crea un camino aleatorio.
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Traza los puntos del recorrido.
    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(
        rw.x_values,
        rw.y_values,
        c=point_numbers,
        cmap=plt.cm.Blues,
        edgecolors="none",
        s=1,
    )

    ax.set_aspect("equal")

    # Enfatiza el primer y último punto.
    ax.scatter(0, 0, c="green", edgecolors="none", s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)

    # Elimina los ejes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Hacer otro camino? (y/n): ")
    if keep_running == "n":
        break
