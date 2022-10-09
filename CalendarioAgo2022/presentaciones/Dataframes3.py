import pandas as pd

productos = [["Laptop","impresora","tablet","escritorio","silla"], [1300, 150, 300, 450,200]]

df = pd.DataFrame(productos).transpose()
df.columns = ["Producto", "Precio"]
print(df)
print("Productos: " + str(type(productos)))
print("df: " + str(type(df)))

promedio = df["Precio"].mean()
maximo = df["Precio"].max()
minimo = df["Precio"].min()

print("El promedio de los precios es: %.2f" % promedio)
print("El máximo precio es: %.2f" % maximo)
print("El minimo precio es: %.2f" % minimo)




