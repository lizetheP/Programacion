import matplotlib.pyplot as plt

estados = ["Oaxaca", "Veracruz", "Puebla", "Chihuahua", "Chiapas", "Sonora", "Zacatecas", "Guerrero", "Durango", "Yucatán", "Nuevo León", "Tamaulipas"]
contingencias = [1002, 271, 567, 288, 108, 211, 312, 125,259, 177, 130, 206]
emergencias = [5868, 5087, 1608, 1646, 1655, 1231, 880, 1029, 881, 762, 783, 568]

plt.title("Situaciones de emergencia y contingencia 2025")
plt.xlabel("Contingencias climatológicas")
plt.ylabel("Emergencias / Desastres")
plt.plot(estados, contingencias, estados, emergencias) 
plt.legend(["Contingencias", "Emergencias"])
plt.xticks(rotation = 45)

plt.show()

"""
RESPUESTA 1:
estados = ["Oaxaca", "Veracruz", "Puebla", "Chihuahua", "Chiapas", "Sonora", "Zacatecas", "Guerrero", "Durango", "Yucatán", "Nuevo León", "Tamaulipas"]
contingencias = [1002, 271, 567, 288, 108, 211, 312, 125,259, 177, 130, 206]
emergencias = [5868, 5087, 1608, 1646, 1655, 1231, 880, 1029, 881, 762, 783, 568]

plt.title("Situaciones de emergencia y contingencia 2025")
plt.xlabel("Contingencias climatológicas")
plt.ylabel("Emergencias / Desastres")
plt.plot(contingencias) 
plt.legend(["Contingencias", "Emergencias"])
plt.xticks(rotation = 45)

plt.show()

RESPUESTA 2:
estados = ["Oaxaca", "Veracruz", "Puebla", "Chihuahua", "Chiapas", "Sonora", "Zacatecas", "Guerrero", "Durango", "Yucatán", "Nuevo León", "Tamaulipas"]
contingencias = [1002, 271, 567, 288, 108, 211, 312, 125,259, 177, 130, 206]
emergencias = [5868, 5087, 1608, 1646, 1655, 1231, 880, 1029, 881, 762, 783, 568]

plt.title("Situaciones de emergencia y contingencia 2025")
plt.xlabel("Contingencias climatológicas")
plt.ylabel("Emergencias / Desastres")
plt.plot(emergencias) 
plt.legend(["Contingencias", "Emergencias"])
plt.xticks(rotation = 45)

plt.show()

RESPUESTA 3:
estados = ["Oaxaca", "Veracruz", "Puebla", "Chihuahua", "Chiapas", "Sonora", "Zacatecas", "Guerrero", "Durango", "Yucatán", "Nuevo León", "Tamaulipas"]
contingencias = [1002, 271, 567, 288, 108, 211, 312, 125,259, 177, 130, 206]
emergencias = [5868, 5087, 1608, 1646, 1655, 1231, 880, 1029, 881, 762, 783, 568]

plt.title("Situaciones de emergencia y contingencia 2025")
plt.xlabel("Contingencias climatológicas")
plt.ylabel("Emergencias / Desastres")
plt.scatter(contingencias, emergencias) 
plt.legend(["Contingencias", "Emergencias"])
plt.xticks(rotation = 45)

plt.show()
"""
