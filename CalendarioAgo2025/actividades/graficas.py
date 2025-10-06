import matplotlib.pyplot as plt

def graficas(x, y1, y2):
    #divide la pantalla en 1 renglón, 2 columnas e inicio en el cuadrante 1
    plt.subplot(121)
    plt.xlabel("Frutas")
    plt.ylabel("Cantidad")
    plt.title("Este mes")
    plt.plot(x, y1, "c*-") # Estrellas color cian unidas por raya continua

    #divide la pantalla en 1 renglón, 2 columnas e inicio en el cuadrante 2
    plt.subplot(122)
    plt.xlabel("Frutas")
    plt.ylabel("Cantidad")
    plt.title("Mes anterior")
    plt.plot(x, y2, "mD:") #"mD:" Diamantes color magenta unidos por dos puntos :

    # Salva la gráfica con el nombre de Graficos.png
    plt.savefig("Graficos.png")

    # Muestra la gráfica
    plt.show()

def main():
    x = ["Peras", "Manzanas", "Plátanos"]
    y1 = [1, 5, 3]
    y2 = [-4, 3, 6]
    graficas(x, y1, y2)
    
main()

