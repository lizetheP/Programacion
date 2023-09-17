import pandas as pd
import openpyxl

tabla = pd.read_excel("vendedores.xlsx")
print(tabla)

nombres = tabla["NOMBRE"]
salarios = tabla["SALARIO"]
print(nombres)

salarioMax = salarios.max()
print("El salario más grande es: $%.2f" % salarioMax)


