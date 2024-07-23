import matplotlib.pyplot as plt
x = ["peras", "manzanas", "plátanos"]
y1 = [1, 5, 3]
y2 = [-4, 3, 6]
#divide la pnatalla en 1 renglón, 2 columnas e inicio en el cuadrante 1
plt.subplot(121)
plt.xlabel("Frutas")
plt.ylabel("Cantidad")
plt.title("Este mes")
plt.plot(x, y1, "g*:")
#divide la pnatalla en 1 renglón, 2 columnas e inicio en el cuadrante 2
plt.subplot(122)
plt.xlabel("Frutas")
plt.ylabel("Cantidad")
plt.title("Mes anterior")
plt.plot(x, y2, "b<-")
plt.show()
plt.savefig("Graficos.png")