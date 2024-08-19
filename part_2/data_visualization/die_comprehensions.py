import plotly.express as px
from die import Die

# Crea dos dados D6.
die_1 = Die()
die_2 = Die()

# Inicializa una lista para las frecuencias.
max_result = die_1.num_sides * die_2.num_sides
frequencies = [0] * (max_result + 1)

# Realiza 1000 tiradas y calcula las frecuencias directamente.
for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    frequencies[result] += 1

# Elimina los resultados que no pueden ocurrir (menores a 2).
poss_results = range(2, max_result + 1)
frequencies = frequencies[2:]

# Visualiza los resultados.
title = "Resultados de lanzar dos D6 1.000 veces"
labels = {"x": "Resultados", "y": "Frecuencia de resultados"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Personalización de gráficos.
fig.update_layout(xaxis_dtick=1)

fig.show()
