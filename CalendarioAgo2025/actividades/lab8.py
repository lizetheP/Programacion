import pandas as pd
import matplotlib.pyplot as plt

def unidades_vendedor(reporte):
    #groupby("COLUMNA").get_group("valor")
    reporteEste = reporte.groupby("REGION").get_group("ESTE")
    print(reporteEste)
    nombres = reporteEste["NOMBRE"]
    print(nombres)
    unidades = reporteEste["UNIDADES VENDIDAS"]
    print(unidades)
    plt.bar(nombres, unidades)
    plt.title("Unidades vendidas por vendedor en la región ESTE")
    plt.xlabel("Vendedores")
    plt.ylabel("Unidades vendidas")
    plt.xticks(rotation = 50)
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
    print("1. Unidades vendidas por vendedor en región ESTE")
    print("2. Salir")
    
def main():
    reporte = pd.read_excel("vendedores.xlsx")
    continua = True
    while continua == True:
        menu()
        opcion = int(input("Dame una opción: "))
        if opcion == 1:
            unidades_vendedor(reporte)
        elif opcion == 2:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")
            
main()

