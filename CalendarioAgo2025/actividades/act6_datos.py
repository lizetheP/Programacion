import pandas as pd
import openpyxl
import statistics
import numpy as np
import matplotlib.pyplot as plt

def main():
    tabla = pd.read_excel("vendedores.xlsx")
    print(tabla)
    nombres = tabla["NOMBRE"]
    print(nombres)
    salarios = tabla["SALARIO"]
    print(salarios)
    salarioMax = salarios.max()
    print("El salario más grande es: ", salarioMax)
    tablaSur = tabla.groupby("REGION").get_group("SUR")
    print(tablaSur)
    
main()
