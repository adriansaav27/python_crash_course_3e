import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Establece el título del gráfico y etiqueta los ejes.
ax.set_title("Cuadrante", fontsize=24)
ax.set_xlabel("Valor", fontsize=14)
ax.set_ylabel("Cuadrado del valor", fontsize=14)

# Establece el tamaño de las etiquetas.
ax.tick_params(labelsize=14)

# Establezca el rango para cada eje.
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style="plain")

# plt.savefig("squares_plot.png", bbox_inches="tight")

plt.show()
