# Demande des trois valeurs à l'utilisateur
a = int(input("Entrez la premiere valeur : "))
b = int(input("Entrez la deuxieme valeur : "))
c = int(input("Entrez la troisieme valeur : "))

# Affichage des valeurs initiales
print(f"Les valeurs entrees sont : a = {a}, b = {b} et c = {c}")
print("Permutation: a ==> b, b ==> c, c ==> a")

# === Début du code à compléter ===
temp = a
a = c
c = b
b = temp
# === Fin du code à compléter ===

# Affichage des valeurs permutées
print(f"Les valeurs permutees sont : a = {a}, b = {b} et c = {c}")