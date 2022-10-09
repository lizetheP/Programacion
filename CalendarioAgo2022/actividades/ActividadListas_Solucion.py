import numpy as np
import statistics

def estadistica(lista):
    print("La máxima calificación que obtuve fue : %.1f" % np.max(lista))
    print("La mínima calificación que obtuve fue : %.1f " % np.min(lista))
    print("Mi promedio es : %.1f" % statistics.mean(lista))
    print("La desviación de mis notas fue : %.1f" % statistics.stdev(lista))
    print("Obtuve %i calificaciones de 100" % lista.count(100))
    print("Obtuve %i calificaciones de 80" % lista.count(80))
    
def crea_lista(tam):
    contador = 1
    lista = []
    while contador <= tam:
        numero = float(input("Dame tu calificación: "))
        lista.append(numero)
        contador = contador + 1
    return lista
    
def main():
    t = int(input("Introduce el tamaño de la lista: "))
    if t > 0:
        lista = crea_lista(t)
        print("Mis calificaciones son: ", lista)
        estadistica(lista)
    else:
        print("Tamaño de lista inválido")
        
main()