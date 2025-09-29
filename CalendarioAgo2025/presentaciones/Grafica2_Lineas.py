import matplotlib.pyplot as plt

estados = ["Oaxaca", "Veracruz", "Puebla", "Chihuahua", "Chiapas", "Sonora"]
contingencias = [1002, 271, 567, 288, 108, 211]
emergencias = [5868, 5087, 1608, 1646, 1655, 1231]

plt.title("Situaciones de emergencia y contingencia")
plt.xlabel("Contingencias climatológicas")
plt.ylabel("Emergencias / Desastres")

#"g*-." Estrellas color verde unidas por raya y puntos alternados
#"b>-" Flechas color azúl unidos por raya continua

plt.plot(estados, contingencias, "g*-.", estados, emergencias, "b>-") 

plt.legend(["Contingencias", "Emergencias"])

#Rotación 45 grados de etiquetas en el eje x
plt.xticks(rotation = 45)

plt.show()