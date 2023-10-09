import pandas as pd
tabla = pd.read_excel("vendedores.xlsx")
#nombres = tabla["NOMBRE"]
#print(nombres)
#salarios = tabla["SALARIO"]
#print(salarios)
#salarioMax = salarios.max()
#print("El salario más grande es: $", salarioMax)
tablaSur = tabla.groupby("REGION").get_group("SUR")
print(tablaSur)