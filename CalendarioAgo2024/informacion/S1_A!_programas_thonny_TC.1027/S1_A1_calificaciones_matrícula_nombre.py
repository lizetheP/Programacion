# Programa 2: Problema 2: Un alumno desea conocer la calificación final de su materia de Programación.
# La rúbrica de esta materia se compone de la siguiente manera: 
# Parcial 1 - 20%,     Parcial 2 - 35%,      Proyecto Final - 15%      y   Examen Final - 30%.

print("Nombre del alumno, matrícula, carrera, semestre")
print("Captura la calificación del primer parcial")
Parcial_1=float(input())
print("Captura la calificación del segundo parcial")
Parcial_2=float(input())
print("Captura la calificación del proyecto final")
Proyecto_Final=float(input())
print("Captura la calificación del examen final")
Examen_Final=float(input())
Calificacion_Final=float(Parcial_1*0.20+Parcial_2*0.35+Proyecto_Final*0.15+Examen_Final*0.3)
print("Tu calificación final en la materia de programación es ",Calificacion_Final)



