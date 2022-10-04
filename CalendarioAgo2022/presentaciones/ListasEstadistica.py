# importo biblioteca numpy para máximo, mínimo
import numpy as np
# importo biblioteca statistics para media, mediana, moda, desviación
import statistics

pesos = [70, 69.5, 71, 69, 70, 68.5, 68]
# Despliego el máximo
print("Máximo = ", np.max(pesos))
# Despliego el mínimo
print("Mínimo = ", np.min(pesos))

# Despliego el promedio
print("Promedio = %.2f" % statistics.mean(pesos))
# Despliego la mediana
print("Mediana = %.2f" % statistics.median(pesos))
# Despliego la moda
print("Moda = %.2f" % statistics.mode(pesos))
