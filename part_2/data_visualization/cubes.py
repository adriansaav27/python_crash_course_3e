import matplotlib.pyplot as plt

# x_values = range(1, 6)
x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(x_values, y_values)

# Establece el título del gráfico y etiqueta los ejes.
ax.set_title("Cubo", fontsize=24)
ax.set_xlabel("Valor", fontsize=14)
ax.set_ylabel("Cubo del valor", fontsize=14)

# Establece el tamaño de las etiquetas.
ax.tick_params(labelsize=14)

plt.show()
