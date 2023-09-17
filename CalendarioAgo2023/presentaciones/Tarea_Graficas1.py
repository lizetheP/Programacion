import matplotlib.pyplot as plt
productos = ["Detergente", "Cepillo", "Cloro", "Escoba", "Recogedor"]
precios = [20.5, 50.1, 18.5, 80.2, 63.4]

barlist=plt.bar(productos, precios)
barlist[0].set_color('r')
barlist[1].set_color('g')
barlist[2].set_color('b')
barlist[3].set_color('c')
barlist[4].set_color('y')
plt.title("Precios de los productos 2022")
plt.xlabel("Productos")
plt.ylabel("Precios")
plt.show()

"""
plt.title("Productos 2022")
plt.xlabel("Productos")
plt.ylabel("Precios")

plt.plot(meses, dolar, "bH", meses, euro, "r>-")
plt.legend(["Dólar", "Euro"])
plt.show()

barlist=plt.bar(["a","b","c","d"], [1,2,3,4])
barlist[0].set_color('r')
barlist[1].set_color('g')
barlist[2].set_color('b')
barlist[3].set_color('c')
plt.show()
"""