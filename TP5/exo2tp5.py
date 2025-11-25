notes = []
coeffs = []


for i in range(1, 6):
    ligne = input(f"Veuillez entrer la note du module {i} et le coefficient correspondant : ")
    # On découpe la chaîne sur l'espace
    morceaux = ligne.split(" ")


    note = float(morceaux[0])
    coeff = int(morceaux[1])

    notes.append(note)
    coeffs.append(coeff)


somme_ponderee = 0
somme_coeffs = 0

for n, c in zip(notes, coeffs):
    somme_ponderee += n * c
    somme_coeffs += c

if somme_coeffs == 0:
    print("La somme des coefficients est nulle, impossible de calculer une moyenne.")
else:
    moyenne = somme_ponderee / somme_coeffs
    print(f"Moyenne générale : {moyenne:.2f}")


    aucune_note_inferieure_a_8 = all(n >= 8 for n in notes)

    if moyenne > 10 and aucune_note_inferieure_a_8:
        print("L'étudiant est admis.")
    else:
        print("L'étudiant n'est pas admis.")