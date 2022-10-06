# importo biblioteca numpy para máximo, mínimo
import numpy as np
# importo biblioteca statistics para media, mediana, moda, desviación
import statistics

calificaciones = [100, 90, 87, 88, 100, 70, 80, 100]
print("Mis calificaciones son: ", calificaciones)
print("Mi promedio es : %.1f" % statistics.mean(calificaciones))
print("La moda de mis calificaciones es : %.1f" % statistics.mode(calificaciones))
print("La máxima calificación que obtuve fue : %.1f" % np.max(calificaciones))
print("La mínima calificación que obtuve fue : %.1f " % np.min(calificaciones))
print("La desviación de mis notas fue : %.1f" % statistics.stdev(calificaciones))
print("Obtuve %i calificaciones de 100" % calificaciones.count(100))
print("Obtuve %i calificaciones de 80" % calificaciones.count(80))