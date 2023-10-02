import matplotlib.pyplot as plt
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto"]
dolar = [20.46, 20.64, 20.43, 19.91, 20.37, 19.69, 20.13, 20.35]
euro = [23.33, 23.18, 22.98, 21.99, 21.56, 21.10, 21.08, 20.83]

plt.subplot(121)
plt.title("Tipo de cambio del dólar 2022")
plt.xlabel("Meses")
plt.ylabel("Tipo de cambio")
plt.tick_params(axis='x', rotation=60)
plt.plot(meses, dolar, "rP-.")

plt.subplot(122)
plt.title("Tipo de cambio del euro 2022")
plt.xlabel("Meses")
plt.ylabel("Tipo de cambio")
plt.plot(meses, euro, "b>-")
plt.tick_params(axis='x', rotation=60)
plt.show()