print("Entrez les moyennes des élèves une par une.")
print("Tapez -1 pour terminer et calculer la moyenne de la classe.")

somme = 0
nb_notes = 0

while True:
    note = float(input("Moyenne de l'élève : "))
    if note == -1:
        break
    somme += note
    nb_notes += 1

if nb_notes > 0:
    moyenne = somme / nb_notes
    print(f"La moyenne de la classe est : {moyenne:.2f}")
else:
    print("Aucune note saisie.")
