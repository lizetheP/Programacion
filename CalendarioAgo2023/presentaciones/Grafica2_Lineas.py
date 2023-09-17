import matplotlib.pyplot as plt
estados = ["Oaxaca", "Veracruz", "Puebla", "Chihuahua", "Chiapas", "Sonora"]
contingencias = [1002, 271, 567, 288, 108, 211]
emergencias = [5868, 5087, 1608, 1646, 1655, 1231]

plt.title("Situaciones de emergencia y contingencia 2022")
plt.xlabel("Contingencias climatológicas")
plt.ylabel("Emergencias / Desastres")

plt.plot(estados, contingencias, "g*", estados, emergencias, "b>-") #b>-
plt.legend(["Contingencias", "Emergencias"])
#plt.xticks(rotation = 45)

plt.show()