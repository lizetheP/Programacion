# Librerías
import matplotlib.pyplot as plt

# Valores de los ejes
ejex = ["SON", "BC", "NL", "JAL", "PUE", "CHIH"]
ejey = [3, 2.3, 4, 4, 7, 5]

# Título del gráfico
plt.title("Promedios año 2024")
# Títulos de los ejes
plt.xlabel("Estados")
plt.ylabel("Promedio")
# Graficando
plt.plot(ejex, ejey)

# Mostrando el gráfico
plt.show()





