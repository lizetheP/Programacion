import matplotlib.pyplot as plt
productos = ["Detergente", "Cepillo", "Cloro", "Escoba", "Recogedor"]
precios = [20.5, 50.1, 18.5, 80.2, 43.4]
ventas = [102.5, 150.3, 185.0, 160.4, 173.6]

plt.subplot(121)
plt.title("Precios de productos")
plt.xlabel("Productos")
plt.ylabel("Precios")
barlist=plt.bar(productos, precios)
barlist[0].set_color('r')
barlist[1].set_color('g')
barlist[2].set_color('b')
barlist[3].set_color('c')
barlist[4].set_color('y')

plt.subplot(122)
plt.title("Ventas de productos")
plt.xlabel("Productos")
plt.ylabel("Precios")
plt.plot(productos, ventas, "rD-.")
plt.show()
