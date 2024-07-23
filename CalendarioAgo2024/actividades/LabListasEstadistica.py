import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics

def estadistica_descriptiva(pesos):
    print()
    print("ESTADISTICA DESCRIPTIVA")
    maximo = np.max(pesos)
    minimo = np.min(pesos)
    promedio = statistics.mean(pesos)
    mediana = statistics.median(pesos)
    moda = statistics.mode(pesos)
    desviacion = statistics.stdev(pesos)
    print("Máximo = %i" % maximo)
    print("Mínimo = %i" % minimo)
    print("Promedio = %.2f" % promedio)
    print("Mediana = %.2f" % mediana)
    print("Moda = %.2f" % moda)
    print("Desviación estándar = %.2f" % desviacion)
    print("El número de 70's es %i" % pesos.count(70))

def tipos_cambio():
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre"]
    dolar = [19.36, 18.89, 18.01, 18.11, 17.91, 17.51, 17.05, 17.29, 17.18]
    euro =  [20.53, 20.65, 19.12, 19.68, 19.76, 18.85, 18.60, 18.90, 18.52]

    plt.title("Tipos de cambio 2023")
    plt.xlabel("Meses")
    plt.ylabel("Dólar / Euro")
    plt.plot(meses, dolar, "rP-.", meses, euro, "b>-")
    plt.legend(["Dólar", "Euro"])
    plt.xticks(rotation=15)
    plt.show()

def tipos_cambio2():
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre"]
    dolar = [19.36, 18.89, 18.01, 18.11, 17.91, 17.51, 17.05, 17.29, 17.18]
    euro =  [20.53, 20.65, 19.12, 19.68, 19.76, 18.85, 18.60, 18.90, 18.52]
    
    #Divide la pantalla en 1 renglón, 2 columnas e inicio en el cuadrante 1
    plt.subplot(121)
    plt.title("Peso vs Dólar")
    plt.xlabel("Meses")
    plt.ylabel("Dólar")
    plt.plot(meses, dolar, "g*:")
    plt.xticks(rotation=40)

    #Divide la pantalla en 1 renglón, 2 columnas e inicio en el cuadrante 2
    plt.subplot(122)
    plt.title("Peso vs Euro")
    plt.xlabel("Meses")
    plt.ylabel("Euro")
    plt.plot(meses, euro, "b<-")
    plt.xticks(rotation=40)
    plt.show()
    
def menu():
    print()
    print("1. Estadística descriptiva")
    print("2. Tipos de cambio en un gráfico")
    print("3. Tipos de cambio en dos gráficos")
    print("4. Salir")
    
def main():
    continua = True
    while continua == True:
        menu()
        opcion = int(input("Dame una opción: "))
        if opcion == 1:
            pesos = [70, 69.5, 71, 69, 70, 68.5, 68]
            estadistica_descriptiva(pesos)
        elif opcion == 2:
            tipos_cambio()
        elif opcion == 3:
            tipos_cambio2()
        elif opcion == 4:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")
    
main()