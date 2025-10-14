import pandas as pd
import matplotlib.pyplot as plt

def cantidad_productos(reporte):
    reporteCondimentos= reporte.groupby("categoria").get_group("Condimento")
    print(reporteCondimentos)
    nombres = reporteCondimentos["nombre"]
    print(nombres)
    cantidad = reporteCondimentos["cantidadExistencia"]
    print(cantidad)

    plt.bar(nombres, cantidad)
    plt.title("Cantidad de productos en existencia de la categoría de Condimentos")
    plt.xlabel("Productos")
    plt.ylabel("Cantidad de productos")
    plt.xticks(rotation = 90)
    plt.show()
    
def precios_productos(reporte):
    reporteFrascos= reporte.groupby("envase").get_group("Frasco")
    print(reporteFrascos)
    nombres = reporteFrascos["nombre"]
    print(nombres)
    precios = reporteFrascos["precioMenudeo"]
    print(precios)
    plt.plot(nombres, precios)
    plt.title("Precios de los productos del tipo de envase Frasco")
    plt.xlabel("Productos")
    plt.ylabel("Precios de menudeo")
    plt.xticks(rotation = 90)
    plt.show()
     
def menu():
    print()
    print("1. Unidades vendidas por vendedor en región ESTE")
    print("2. Promedio de ventas por región")
    print("3. Salir")
    
def main():
    reporte = pd.read_excel("inventario.xlsx")
    print(reporte)
    continua = True
    while continua == True:
        menu()
        opcion = int(input("Dame una opción: "))
        if opcion == 1:
            cantidad_productos(reporte)
        elif opcion == 2:
            precios_productos(reporte)
        elif opcion == 3:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")
            
main()
