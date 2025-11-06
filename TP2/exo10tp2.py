
print("Calcul de la moyenne pondérée pour plusieurs élèves.")
print("Entrez -1 comme nom pour arrêter.")

while True:
    nom = input("\nNom de l'élève : ")
    if nom == "-1":
        break

    somme_ponderee = 0
    somme_coef = 0

    print(f"Entrez les notes de {nom} (note = -1 pour terminer).")
    while True:
        note = float(input("  Note : "))
        if note == -1:
            break
        coef = float(input("  Coefficient : "))
        somme_ponderee += note * coef
        somme_coef += coef

    if somme_coef > 0:
        moyenne = somme_ponderee / somme_coef
        print(f"La moyenne de {nom} est : {moyenne:.2f}")
    else:
        print(f"Aucune note saisie pour {nom}.")

