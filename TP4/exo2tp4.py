while True:
    try:
        nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
        if nombreEtudiants > 0:
            break
        print("Le nombre d'étudiants doit être un entier strictement positif.")
    except ValueError:
        print("Veuillez saisir un entier valide.")

notes = []
somme = 0.0
for i in range(nombreEtudiants):
    while True:
        try:
            note = float(input(f"Note etudiant {i} : "))
            if 0.0 <= note <= 20.0:
                break
            print("La note doit être comprise entre 0 et 20 !")
        except ValueError:
            print("Veuillez saisir une note réelle.")
    notes.append(note)
    somme += note


moyenne = somme / nombreEtudiants


print(f"Moyenne de classe : {moyenne:.2f}")
print("Numéro de l’Etudiant | note | ecart a la moyenne")
for i, n in enumerate(notes):
    print(f"{i} | {n} | {n - moyenne:.2f}")