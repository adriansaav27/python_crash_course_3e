import plotly.express as px
from die import Die

# Crea dos dados, un D6 y un D10.
die_1 = Die()
die_2 = Die(10)

# Se hacen algunas tiradas y guarda los resultados en una lista.
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analiza los resultados.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualiza los resultados.
title = "Resultados de lanzar dos dados, un D6 y un D10 50.000 veces"
labels = {"x": "Resultados", "y": "Frecuencia de resultados"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Personalización de gráficos.
fig.update_layout(xaxis_dtick=1)

fig.show()
# fig.write_html('dice_visual_d6d10.html')
