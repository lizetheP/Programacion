import pandas as pd
import statistics
import numpy as np
import matplotlib.pyplot as plt

def cantidad_productos(reporte):
    #groupby("COLUMNA").get_group("valor")
    reporteCondimentos = reporte.groupby("categoria").get_group("Condimento")
    #print(reporteCondimentos)
    nombres = reporteCondimentos["nombre"]
    #print(nombres)
    cantidad = reporteCondimentos["cantidadExistencia"]
    #print(cantidad)
    plt.bar(nombres, cantidad)
    plt.title("Cantidad de productos en existencia de la categoría de Condimentos")
    plt.xlabel("Productos")
    plt.ylabel("Cantidad de productos")
    plt.xticks(rotation = 90)
    plt.show()
    
def precios_productos(reporte):
    #groupby("COLUMNA").get_group("valor")
    reporteFrascos = reporte.groupby("envase").get_group("Frasco")
    #print(reporteFrascos)
    nombres = reporteFrascos["nombre"]
    #print(nombres)
    precios = reporteFrascos["precioMenudeo"]
    #print(precios)
    plt.plot(nombres, precios, "rD-.")
    plt.title("Precios de los productos del tipo de envase Frasco")
    plt.xlabel("Productos")
    plt.ylabel("Precios de menudeo")
    plt.xticks(rotation = 90)
    plt.show()
    
def promedio_ventas_region(reporte):
    regiones = ["SUR", "NORTE", "ESTE", "OESTE"]
    promedio_ventas = []
    for region in regiones:
        reportexRegion = reporte.groupby("REGION").get_group(region)
        ventasxRegion = reportexRegion["VENTAS TOTALES"]
        promedio = ventasxRegion.mean()
        promedio_ventas.append(promedio)
    #print(promedio_ventas)
    barlist = plt.bar(regiones, promedio_ventas)
    barlist[0].set_color('r')
    barlist[1].set_color('g')
    barlist[2].set_color('b')
    barlist[3].set_color('c')
    plt.title("Promedio de ventas por region")
    plt.xlabel("Regiones")
    plt.ylabel("Promedio de ventas")
    plt.show()
      
def menu():
    print()
    print("1. Cantidad de productos")
    print("2. Precio de productos")
    print("3. Promedio de ventas por región")
    print("4. Salir")
    
def main():
    #print(reporte)
    continua = True
    while continua == True:
        menu()
        opcion = int(input("Dame una opción: "))
        if opcion == 1:
            cantidad_productos(reporte)
        elif opcion == 2:
            precios_productos(reporte)
        elif opcion == 3:
            promedio_ventas_region(reporte)
        elif opcion == 4:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")
            
main()

