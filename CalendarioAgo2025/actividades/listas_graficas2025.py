import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics

# -------------------------------------------------------------------
# --------- Estadística descriptiva ---------------------------------
# -------------------------------------------------------------------

def estadistica(pesos):
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

def main():
    pesos = [70, 69.5, 71, 69, 70, 68.5, 68]
    estadistica(pesos)

main()