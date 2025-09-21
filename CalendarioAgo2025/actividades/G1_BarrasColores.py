# Librerías
import matplotlib.pyplot as plt
# Valores eje X
paises = ["Estados unidos", "España", "México", "Rusia", "Japón"]
# Valores eje Y
ventas = [25, 32, 34, 20, 25]
# Graficando
barras = plt.bar(paises, ventas)
# Colocando colores a las barras
barras[0].set_color('b')
barras[1].set_color('g')
barras[2].set_color('r')
barras[3].set_color('c')
barras[4].set_color('m')
# Mostrando el gráfico
plt.show()



