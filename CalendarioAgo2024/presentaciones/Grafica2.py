import matplotlib.pyplot as plt
estados = ["Oaxaca", "Veracruz"]
contingencias = [1002, 271]
emergencias = [5868, 5087]

plt.xlabel("Contingencias climatológicas")
plt.ylabel("Emergencias / Desastres")
plt.title("Situaciones de emegrencia y contingencia")

plt.plot(estados, contingencias, "g*", estados, emergencias, "b>-")
plt.legend(["Contingencias", "Emergencias"])
plt.xticks(rotation = 45)

plt.show()