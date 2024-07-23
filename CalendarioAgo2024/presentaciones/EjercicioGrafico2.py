import matplotlib.pyplot as plt

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto"]
dolar = [20.46, 20.64, 20.43, 19.91, 20.37, 19.69, 20.13, 20.35]
euro = [23.33, 23.18, 22.98, 21.99, 21.56, 21.10, 21.08, 20.83]

plt.subplot(121)
plt.title("Tipo de cambio Dólar 2022")
plt.xlabel("Meses")
plt.ylabel("Dólar")
plt.plot(meses, dolar, "r*:")
plt.xticks(rotation = 45)

plt.subplot(122)
plt.title("Tipo de cambio Euro 2022")
plt.xlabel("Meses")
plt.ylabel("Euro")
plt.plot(meses, euro, "b<-")
plt.xticks(rotation = 45)
plt.show()

#plt.plot(meses, dolar, "bH", meses, euro, "r>-")
#plt.legend(["Dólar", "Euro"])
#plt.show()
