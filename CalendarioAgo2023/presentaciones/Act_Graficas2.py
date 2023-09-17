import matplotlib.pyplot as plt
productos = ["Detergente", "Cepillo", "Cloro", "Escoba", "Recogedor"]
precios = [20.5, 50.1, 18.5, 80.2, 43.4]
ventas = [102.5, 150.3, 185.0, 160.4, 173.6]

plt.subplot(121)
plt.title("Precios de los productos")
plt.xlabel("Productos")
plt.ylabel("Precios")
plt.plot(productos, precios, "r*:")
#plt.xticks(rotation = 45)

plt.subplot(122)
plt.title("Ventas de productos")
plt.xlabel("Productos")
plt.ylabel("Precios")
plt.plot(productos, ventas, "b<-")
#plt.xticks(rotation = 45)
plt.show()
