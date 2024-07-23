import pandas as pd
#import openpyxl

tabla = pd.read_excel("vendedores.xlsx")
print(tabla)

tablaSur = tabla.groupby("REGION").get_group("SUR")
print(tablaSur)

