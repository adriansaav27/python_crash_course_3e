import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Establece el título del gráfico y etiqueta los ejes.
ax.set_title("Cuadrante", fontsize=24)
ax.set_xlabel("Valor", fontsize=14)
ax.set_ylabel("Cuadrado del valor", fontsize=14)

# Establece el tamaño de las etiquetas.
ax.tick_params(labelsize=14)

plt.show()
