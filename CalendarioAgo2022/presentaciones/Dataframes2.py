import pandas as pd

productos = [["laptop",1300],["impresora",150],["tablet",300],["escritorio",450],["silla",200]]

df = pd.DataFrame(productos, columns = ["Producto", "Precio"])
print(df)