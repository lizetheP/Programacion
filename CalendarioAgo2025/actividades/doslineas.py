import matplotlib.pyplot as plt

def dos_lineas(estados, contingencias, emergencias):
    plt.title("Situaciones de emergencia y contingencia")
    plt.xlabel("Contingencias climatológicas")
    plt.ylabel("Emergencias / Desastres")

    #"r*-." Estrellas color rojo unidas por raya y puntos alternados
    #"g>-" Flechas color verde unidos por raya continua
    plt.plot(estados, contingencias, "r*-.", estados, emergencias, "g>-") 
    plt.legend(["Contingencias", "Emergencias"])

    #Rotación 45 grados de etiquetas en el eje x
    #plt.xticks(rotation = 45)

    plt.show()
    
def main():
    estados = ["Oaxaca", "Veracruz", "Puebla", "Chihuahua", "Chiapas", "Sonora"]
    contingencias = [1002, 271, 567, 288, 108, 211]
    emergencias = [5868, 5087, 1608, 1646, 1655, 1231]
    dos_lineas(estados, contingencias, emergencias)

main()
    

