import numpy as np
import statistics
import matplotlib.pyplot as plt
import pandas as pd
import xlrd
import openpyxl

def promedio_ventas (reporteNorte):
    #promedio = reporteNorte["VENTAS TOTALES"].mean()
    ventasNorte = reporteNorte["VENTAS TOTALES"]
    print(ventasNorte)
    promedio = ventasNorte.mean()
    promedio1 = np.mean(ventasNorte)
    promedio2 = statistics.mean(ventasNorte)
    print("El promedio de ventas de la región norte es: ", promedio)
    print("El promedio de ventas de la región norte es: ", promedio1)
    print("El promedio de ventas de la región norte es: ", promedio2)

def grafica1(reporteNorte):
    vendedoresNorte = reporteNorte["NOMBRE"]
    salariosNorte = reporteNorte["SALARIO"]
    #print(vendedoresNorte)
    #print(salariosNorte)
    plt.bar(vendedoresNorte, salariosNorte)
    plt.title("Salarios de vendedores región norte")
    plt.xlabel("Vendedores")
    plt.ylabel("Salarios")
    plt.xticks(rotation = 45)
    plt.show()

def grafica2(reporteNorte):
    vendedoresNorte = reporteNorte["NOMBRE"]
    ventasNorte = reporteNorte["VENTAS TOTALES"]
    #print(vendedoresNorte)
    #print(salariosNorte)
    plt.plot(vendedoresNorte, ventasNorte, "ro-.")
    plt.title("Ventas de la región norte")
    plt.xlabel("Vendedores")
    plt.ylabel("Ventas")
    plt.xticks(rotation = 90)
    plt.show()
    
def menu():
    print()
    print("1. Promedio de ventas")
    print("2. Gráfica de salarios")
    print("3. Gráfica de ventas")
    print("4. Salir")
    
def main():
    #Carga la información del archivo de Excel en un Dataframe.
    #Crea una lista con las claves permitidas y llama a la función valida_clave.
    continua = True
    while continua == True:
        menu()
        opcion = int(input("Dame una opción: "))
        if opcion == 1:
            
        elif opcion == 2:
            
        elif opcion == 3:
            
        elif opcion == 4:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")

main()