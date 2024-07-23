import matplotlib.pyplot as plt

def grafica_barras():
    paises = ["Estados Unidos", "España", "México", "Rusia", "Japón"]
    ventas = [25, 32, 34, 20, 25]
    # Título del gráfico
    plt.title("Ventas en distintos paises")
    # Leyenda de lo que se grafica
    plt.legend(["Ventas"])
    # Título de los ejes
    plt.xlabel("Paises")
    plt.ylabel("Ventas")
    barrasLista = plt.bar(paises, ventas)
    barrasLista[0].set_color('r')
    barrasLista[1].set_color('g')
    barrasLista[2].set_color('b')
    barrasLista[3].set_color('m')
    barrasLista[4].set_color('c')
    plt.xticks(rotation=15)
    plt.show()

def grafica_linea():
    ejex = ["SON", "BC", "NL", "JAL", "PUE", "CHIH"]
    ejey = [3, 2.3, 4, 4, 7, 5]
    plt.title("Promedios año 2023")
    plt.xlabel("Estados")
    plt.ylabel("Promedio")
    plt.plot(ejex, ejey)
    plt.show()

def grafica_dos_lineas():
    estados = ["Oaxaca", "Veracruz", "Puebla", "Chihuahua", "Chiapas", "Sonora"]
    contingencias = [1002, 27, 567, 288, 108, 211]
    emergencias = [5868, 5087, 1608, 1646, 1655, 1231]

    plt.title("Situaciones de emergencia y contingencia 2023")
    plt.xlabel("Contingencias climatológicas")
    plt.ylabel("Emergencias / Desastres")
    plt.plot(estados, contingencias, "rP-.", estados, emergencias, "b>-")
    plt.legend(["Contingencias", "Emergencias"])
    plt.xticks(rotation=15)
    plt.show()

def dos_graficas():
  x = ["peras", "manzanas", "plátanos"]
  y1 = [1,5,3]
  y2 = [-4, 3, 6]

  #Divide la pantalla en 1 renglón, 2 columnas e inicio en el cuadrante 1
  plt.subplot(121)
  plt.title("Este mes")
  plt.xlabel("Frutas")
  plt.ylabel("Cantidad")
  plt.plot(x, y1, "g*:")

  #Divide la pantalla en 1 renglón, 2 columnas e inicio en el cuadrante 2
  plt.subplot(122)
  plt.title("Mes anterior")
  plt.xlabel("Frutas")
  plt.ylabel("Cantidad")
  plt.plot(x, y2, "b<-")
  plt.show()
  
def main():
    dos_graficas()

main()