import pandas as pd
import matplotlib.pyplot as plt
#import openpyxl

informe = pd.read_excel("ChartData.xlsx")
print(informe)

valoresCierre = informe["Close/Price"]
print(valoresCierre)
promedio = valoresCierre.mean()
print("Promedio del valor de las acciones al final del día: %.2f" % promedio)

cantidad = informe["Volume"]
print(cantidad)
minimo = cantidad.min()
print("La cantidad de transacciones mínima en un día fue: %.2f" % minimo)

fechas = informe["Date"]
print(fechas)
volumen = informe["Volume"]
print(volumen)
"""
plt.title("Cantidad de transacciones por día")
plt.xlabel("Fechas")
plt.ylabel("Cantidad de transacciones")
plt.plot(fechas, volumen, "rD-.")
plt.show()
"""
fechas = informe["Date"]
plt.title("Valor de las acciones al final del día")
plt.xlabel("Fechas")
plt.ylabel("Valor de las acciones al final del día")
plt.plot(fechas, cantidad, "rD-.")
plt.show()
"""
reporte.groupby("REGION").get_group("NORTE")
print(reporteNorte)

ventasNorte = reporteNorte["VENTAS TOTALES"]
print(ventasNorte)

promedioVentas = ventasNorte.mean()
print("Promedio de ventas: %.2f" % promedioVentas)

vendedoresNorte = reporteNorte["NOMBRE"]
print(vendedoresNorte)

salariosNorte = reporteNorte["SALARIO"]
print(salariosNorte)

plt.title("Salarios de los vendedores de la región Norte")
plt.xlabel("Vendedores")
plt.ylabel("Salarios")
barlist=plt.bar(vendedoresNorte, salariosNorte)
barlist[0].set_color('r')
barlist[1].set_color('g')
barlist[2].set_color('b')
barlist[3].set_color('c')
barlist[4].set_color('y')
barlist[5].set_color('r')
barlist[6].set_color('g')
barlist[7].set_color('b')
barlist[8].set_color('c')
barlist[9].set_color('y')

plt.show()
"""