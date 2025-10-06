# Librerías
import matplotlib.pyplot as plt

def barras_simple(paises, ventas):
    # Graficando
    plt.bar(paises, ventas)
    # Mostrando el gráfico
    plt.show()
  
def main():
    # Valores eje X
    paises = ["Estados unidos", "España", "México", "Rusia", "Japón"]
    # Valores eje Y
    ventas = [25, 32, 34, 20, 25]
    barras_simple(paises, ventas)

main()
    

