import matplotlib.pyplot as plt

ejex = ["SON", "BC", "NL", "JAL", "PUE", "CHIH"]
ejey = [3, 2.3, 4, 4, 7, 5]
plt.plot(ejex, ejey)
plt.title("Promedios año 2020")
plt.legend(["Promedios"])
plt.xlabel("Estados")
plt.ylabel("Promedio")
plt.show()