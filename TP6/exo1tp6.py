L1 = [0]*3
print("Liste :", L1)
print("Type :", type(L1))
print("ID :", id(L1))

for i in range(len(L1)):
    print(f"Element {i} - Valeur: {L1[i]}, Type: {type(L1[i])}, ID: {id(L1[i])}")

print("\nRemarque : Tous les éléments ont le même identifiant !")
print("Ils pointent tous vers le même objet en mémoire (le même 0).")

L1[1] = L1[1] + 1
print("Liste modifiée :", L1)
print("Type :", type(L1))
print("ID :", id(L1))

print("\nRéponse : L'ID de la liste n'a pas changé.")
print("La liste est mutable, on peut modifier son contenu sans créer")
print("un nouvel objet liste.")

for i in range(len(L1)):
    print(f"Element {i} - Valeur: {L1[i]}, Type: {type(L1[i])}, ID: {id(L1[i])}")

print("\nRéponse : Un nouvel objet a été créé pour l'élément modifié !")
print("Conclusion : Les entiers sont immutables en Python.")
print("L'incrémentation crée un nouvel objet et fait pointer")
print("l'élément de la liste vers ce nouvel objet.")

machaine = "machaine"
print("Variable :", machaine)
print("Type :", type(machaine))
print("ID :", id(machaine))
print()

for i in range(len(machaine)):
    print(f"Caractere {i} - Valeur: '{machaine[i]}', Type: {type(machaine[i])}, ID: {id(machaine[i])}")

print("\nRemarque : Les caractères identiques (comme les deux 'a')")
print("partagent le même identifiant.")
print("Python optimise la mémoire en réutilisant les mêmes objets")
print("immutables (string interning pour les caractères).")