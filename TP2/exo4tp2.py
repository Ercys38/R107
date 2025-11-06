# Fondue.py

# 1. Déclaration de la constante BASE
BASE = 4

# 2 à 5. Déclaration des quantités de base pour 4 personnes
fromage = 800.0  # en grammes
eau = 2.0        # en décilitres
ail = 2.0        # en gousses
pain = 400.0     # en grammes

# 6. Demande du nombre de convives
nbConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue : "))

# 8. Calcul des quantités adaptées
fromage = fromage * nbConvives / BASE
eau = eau * nbConvives / BASE
ail = ail * nbConvives / BASE
pain = pain * nbConvives / BASE

# 9. Affichage de la recette adaptée
print(f"\nPour faire une fondue fribourgeoise pour {nbConvives} personnes, il vous faut :")
print(f"- {fromage} gr de fromage")
print(f"- {eau} dl d'eau")
print(f"- {ail} gousse(s) d'ail")
print(f"- {pain} gr de pain")
