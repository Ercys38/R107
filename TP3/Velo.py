while True:
    debut = int(input("Donnez l’heure de début de la location (un entier) : "))
    fin = int(input("Donnez l’heure de fin de la location (un entier) : "))

    if not (0 <= debut <= 24) or not (0 <= fin <= 24):
        print("Les heures doivent être comprises entre 0 et 24 !")
        continue
    if debut == fin:
        print("Attention ! l’heure de fin est identique à l’heure de début.")
        continue
    if debut > fin:
        print("Attention ! le début de la location est après la fin ...")
        continue

    heures_tarif_1 = 0
    heures_tarif_2 = 0

    for h in range(debut, fin):
        if (0 <= h < 7) or (17 <= h < 24):
            heures_tarif_1 += 1
        else:
            heures_tarif_2 += 1

    total = heures_tarif_1 * 1.0 + heures_tarif_2 * 2.0

    print("Vous avez loué votre vélo pendant")
    if heures_tarif_1 > 0:
        print(f"{heures_tarif_1} heure(s) au tarif horaire de 1.0 euro(s)")
    if heures_tarif_2 > 0:
        print(f"{heures_tarif_2} heure(s) au tarif horaire de 2.0 euro(s)")
    print(f"Le montant total à payer est de {total:.1f} euro(s).")
    break