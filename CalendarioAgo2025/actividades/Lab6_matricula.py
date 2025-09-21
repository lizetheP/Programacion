import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics

def estadistica_descriptiva(pesos):
    print()
    print("ESTADÍSTICA DESCRIPTIVA")
    print()
    print("Pesos: ", pesos)
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

def tipos_cambio(meses, dolar, euro):

    plt.title("Tipos de cambio 2024")
    plt.xlabel("Meses")
    plt.ylabel("Dólar / Euro")
    plt.plot(meses, dolar, "m>:", meses, euro, "gH-")
    plt.legend(["Dólar", "Euro"])
    plt.show()

def tipos_cambio2(meses, dolar, euro):

    #Divide la pantalla en 1 renglón, 2 columnas e inicio en el cuadrante 1
    plt.subplot(121)
    plt.title("Peso vs Dólar")
    plt.xlabel("Meses")
    plt.ylabel("Dólar")
    plt.xticks(rotation = 45)
    plt.plot(meses, dolar, "g*:")

    #Divide la pantalla en 1 renglón, 2 columnas e inicio en el cuadrante 2
    plt.subplot(122)
    plt.title("Peso vs Euro")
    plt.xlabel("Meses")
    plt.ylabel("Euro")
    plt.plot(meses, euro, "b<-")
    plt.xticks(rotation = 45)
    plt.show()

def menu():
    print()
    print("1. Estadística descriptiva")
    print("2. Tipos de cambio en un gráfico")
    print("3. Tipos de cambio en dos gráficos")
    print("4. Salir")
    
def main():
    pesos = [70, 69.5, 71, 69, 70, 68.5, 68]
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre"]
    dolar = [16.90, 17.04, 16.72, 16.71, 16.68, 18.46, 17.73, 18.65, 19.16]
    euro =  [18.50, 18.36, 18.20, 17.75, 18.17, 19.76, 19.32, 20.46, 21.25]
    continua = True
    while continua == True:
        menu()
        opcion = int(input("Dame una opción: "))
        if opcion == 1:
            estadistica_descriptiva(pesos)
        elif opcion == 2:
            tipos_cambio(meses, dolar, euro)
        elif opcion == 3:
            tipos_cambio2(meses, dolar, euro)
        elif opcion == 4:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")
        
main()