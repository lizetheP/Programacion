import pandas as pd

productos = ["Laptop", "Impresora", "Tablet", "Escritorio", "Silla"]

df = pd.DataFrame(productos, columns = ["Nombre del producto"])
print(df)