import pandas as pd
import matplotlib.pyplot as plt
#import openpyxl

reporte = pd.read_excel("vendedores.xlsx")
print(reporte)

reporteNorte = reporte.groupby("REGION").get_group("NORTE")
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
