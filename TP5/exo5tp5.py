heures = float(input("Entrez le nombre d'heures travaillées : "))
taux_horaire = float(input("Entrez le salaire horaire (en euros) : "))

salaire = 0.0

if heures <= 160:

    salaire = heures * taux_horaire
else:

    salaire = 160 * taux_horaire
    heures_restantes = heures - 160

    if heures_restantes <= 40:

        salaire += heures_restantes * taux_horaire * 1.25
    else:

        salaire += 40 * taux_horaire * 1.25
        heures_restantes -= 40

        salaire += heures_restantes * taux_horaire * 1.50

print(f"Le salaire de l'ouvrier est de {salaire:.2f} euros.")