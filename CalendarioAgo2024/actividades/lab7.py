import pandas as pd
import statistics
import numpy as np
import matplotlib.pyplot as plt

def promedio_ventas(ventasNorte):
    promedio = np.mean(ventasNorte)
    promedio2 = statistics.mean(ventasNorte)
    promedio3 = ventasNorte.mean()
    print("El promedio de ventas de la región norte es: %.2f" % promedio)
    print("El promedio de ventas de la región norte es: %.2f" % promedio2)
    print("El promedio de ventas de la región norte es: %.2f" % promedio3)
    
def grafica1(vendedoresNorte, salariosNorte):
    plt.bar(vendedoresNorte, salariosNorte)
    plt.title("Salario de los vendedores")
    plt.xlabel("Vendedores")
    plt.ylabel("Salarios")
    plt.xticks(rotation = 90)
    plt.show()

def grafica2(vendedoresNorte, ventasNorte):
    plt.title("Ventas de los vendedores")
    plt.xlabel("Vendedores")
    plt.ylabel("Ventas")
    plt.plot(vendedoresNorte, ventasNorte, "ro-.")
    plt.xticks(rotation = 90)
    plt.show()
    
def menu():
    print()
    print("1. Promedio de ventas")
    print("2. Gráfica 1")
    print("3. Gráfica 2")
    print("4. Salir")
    
def main():
    reporte = pd.read_excel("vendedores.xlsx")
    reporteNorte = reporte.groupby("REGION").get_group("NORTE")
    #print(reporteNorte)

    ventasNorte = reporteNorte["VENTAS TOTALES"]
    #print(ventasNorte)
   
    vendedoresNorte = reporteNorte["NOMBRE"]
    #print(vendedoresNorte)

    salariosNorte = reporteNorte["SALARIO"]
    #print(salariosNorte)
    
    continua = True
    while continua == True:
        menu()
        opcion = int(input("Dame una opción: "))
        if opcion == 1:
            promedio_ventas(ventasNorte)
        elif opcion == 2:
            grafica1(vendedoresNorte, salariosNorte)
        elif opcion == 3:
            grafica2(vendedoresNorte, ventasNorte)
        elif opcion == 4:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")

main()

