import pandas as pd
import matplotlib.pyplot as plt

print("Andrea Del Toro A01705606")

informe = pd.read_excel("ChartData.xlsx")
valorescierre = informe["Close/Price"]
print(valorescierre)
promedio = valorescierre.mean()
print("Promedio del valor de las acciones al final del día: %.2f" % promedio)
cantidad = informe["Volume"]
print(cantidad)
minimo = cantidad.min()
print("La cantidad de transacciones mínima en un día fue: %.2f" % minimo)
fecha = informe["Date"]

plt.plot(fecha, valorescierre, "b.-")
plt.title("Valor de las acciones al final del dia")
plt.xlabel("Valores")
plt.ylabel("Fecha")
plt.show()