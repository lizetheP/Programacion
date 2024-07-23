#Programa 1. COnvertir el precio de un producto de pesos a dólares
# si se tiene el tipo de cambio del dolár y el precio en pesos del producto
# el resultado debe mostrar "el precio del producto en dolares es:", X

print("Nombre del alumno, matrícula, carrera, semestre")
print("Captura el tipo de cambio actual del dolar")
Tipo_cambio=float(input())
print("Captura el precio del producto en pesos M/N ")
Precio_pesos=float(input())
Precio_dolares=float(Precio_pesos/Tipo_cambio)
print("El precio en dólares del producto es $",Precio_dolares)


