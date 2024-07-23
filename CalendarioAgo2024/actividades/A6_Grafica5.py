import matplotlib.pyplot as plt
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto"]
dolar = [20.46, 20.64, 20.43, 19.91, 20.37, 19.69, 20.13, 20.35]
euro = [23.33, 23.18, 22.98, 21.99, 21.56, 21.10, 21.08, 20.83]

plt.title("Tipo de cambio del dólar y el euro 2022")
plt.xlabel("Meses")
plt.ylabel("Tipo de cambio")
plt.plot(meses, dolar, "rP-.", meses, euro, "b>-")
plt.show()

"""

#Divide la pantalla en 1 renglón, 2 columnas e inicio en el cuadrante 1
plt.subplot(121)
plt.xlabel("Frutas")
plt.ylabel("Cantidad")
plt.title("Este mes")
plt.plot(x, y1, "g*:")

#Divide la pantalla en 1 renglón, 2 columnas e inicio en el cuadrante 2
plt.subplot(122)
plt.xlabel("Frutas")
plt.ylabel("Cantidad")
plt.title("Mes anterior")
plt.plot(x, y2, "b<-")
plt.show()
"""