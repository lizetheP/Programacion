# crar listas desde cero
import pandas as pd
import numpy as np
total = int(input("Dígame cuántos números tiene la lista: "))
contador=0
if total < 1:
    print("¡Imposible!")
else:
    lista = []
    while total > contador:
        numero = int(input("Dame un número  "))
        lista =lista + [numero]
        contador=contador+1
    print("La lista creada es:", lista)
    
# usar una lista creada y obtener algunas funciones con ella    
import numpy as np
import statistics
otra_lista = [5,2,5,6,1,2,6,7,2,6,3,5,5]
x = statistics.mean(otra_lista)
print("el promedio", x)
y = statistics.median(otra_lista)
print("la mediana", y)
z = statistics.mode(otra_lista)
print("la que mas se repite",z)
a = statistics.stdev(otra_lista)
print("desviación estandar", a)
# ahora con la libreria numpy
# valor máximo de la lista
max= np.max(otra_lista)
print ("el mayor", max)
# valor mínimo de la lista
min= np.min(otra_lista)
print ("el menor", min)
# para saber cuantas veces se repite un valor dado por el usuario
valor= int(input( "que valor quieres saber cuantas veces esta"))
contar= otra_lista.count(valor) 
print ("cuantos", valor, "son", contar)