# importo biblioteca numpy para máximo, mínimo
import numpy as np
# importo biblioteca statistics para media, mediana, moda, desviación estándar
import statistics
pesos = [70, 69.5, 71, 69, 70, 68.5, 68]
# Despliego el máximo
maximo = np.max(pesos)
print("Máximo = ", maximo)
# Despliego el mínimo
minimo = np.min(pesos)
print("Mínimo = ", minimo)

# Despliego el promedio
promedio = statistics.mean(pesos)
print("Promedio = %.2f" % promedio)
# Despliego la mediana
mediana = statistics.median(pesos)
print("Mediana = %.2f" % mediana)
# Despliego la moda
moda = statistics.mode(pesos)
print("Moda = %.2f" % moda)
# Despliego la desviación estándar
desviacion = statistics.stdev(pesos)
print("Desviación estandar = %.2f" % desviacion)
