import matplotlib.pyplot as plt
from die_walk import RandomWalk
from die import Die

# Crea un dado D6.
die = Die()
num_tiradas = 10

# Matplotlib
x_values = range(1, num_tiradas + 1)

# Se hacen algunas tiradas y guarda los resultados en una lista.
results = []
for roll_num in range(num_tiradas):
    result = die.roll()
    results.append(result)

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(x_values, results, linewidth=3)

# Establece el título del gráfico y etiqueta los ejes.
ax.set_title(f"Resultados de lanzar un D6 {num_tiradas} veces", fontsize=14)
ax.set_xlabel("Num. Tiradas", fontsize=14)
ax.set_ylabel("Valor", fontsize=14)

# Establece el tamaño de las etiquetas.
ax.tick_params(labelsize=14)

plt.show()

# Plotly
# Crea un camino aleatorio.
# rw = RandomWalk(num_tiradas)
# rw.fill_walk(die)

# Traza los puntos del recorrido.
# plt.style.use("classic")
# fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
# point_numbers = range(rw.num_points)
# ax.scatter(
#   rw.x_values,
# rw.y_values,
# s=100,
# )

# ax.set_aspect("equal")

# plt.show()
