import matplotlib.pyplot as plt
productos = ["Detergente", "Cepillo", "Cloro", "Escoba", "Recogedor"]
precios = [20.5, 50.1, 18.5, 80.2, 63.4]
ventas = [100, 40, 80, 30, 20]

plt.title("Precio y ventas de Productos 2022")
plt.xlabel("Productos")
plt.ylabel("Precios / Ventas")

plt.plot(productos, precios, "b:", productos, ventas, "r>-")
plt.legend(["Precios", "Ventas"])
plt.show()

