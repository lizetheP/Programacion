import pandas as pd
import openpyxl
import statistics
import numpy as np
import matplotlib.pyplot as plt

def barras(vendedoresNorte, salariosNorte):
    # Título del gráfico
    plt.title("Salarios de los vendedores en la región Norte")

    # Títulos de los ejes
    plt.xlabel("Vendedor")
    plt.ylabel("Salario")
    # Graficando
    plt.bar(vendedoresNorte, salariosNorte)
    
    plt.xticks(rotation = 45)
    
    # Mostrando el gráfico
    plt.show()
    
def main():
    reporte = pd.read_excel("vendedores.xlsx")
    #print(reporte)
    reporteNorte = reporte.groupby("REGION").get_group("NORTE")
    #print(reporteNorte)
    ventasNorte = reporteNorte["VENTAS TOTALES"]
    #print(ventasNorte)
    print("El promedio de ventas es: %.2f" % ventasNorte.mean())
    vendedoresNorte = reporteNorte["NOMBRE"]
    #print(vendedoresNorte)
    salariosNorte = reporteNorte["SALARIO"]
    #print(salariosNorte)
    barras(vendedoresNorte, salariosNorte)
    
    
main()
