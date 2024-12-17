import matplotlib.pyplot as plt

# Données d'exemple pour les courbes (ajoutez vos propres points)
rappel_BM25 = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
precision_BM25 = [0.6, 0.4, 0.3, 0.28, 0.24, 0.2, 0.15, 0.12, 0.09, 0.05, 0.01]

# Assurez-vous que les axes fusionnent au (0,0)
plt.plot(rappel_BM25, precision_BM25, 'o-', label="Baseline BM25")

# Configurations pour fusionner les axes
plt.xlim(0, 1)  # L'axe X commence à 0
plt.ylim(0, 0.7)  # Ajuster pour inclure le point zéro

# Ajouter les titres et légendes
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("Courbes Precision-Recall")
plt.axhline(y=0, color='gray', linestyle='--')  # Ligne horizontale pour 0
plt.axvline(x=0, color='gray', linestyle='--')  # Ligne verticale pour 0
plt.legend()
plt.grid()

# Afficher le graphe
plt.show()