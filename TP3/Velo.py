def saisir_heure(prompt):
    while True:
        try:
            h = int(input(prompt))
            if 0 <= h <= 23:
                return h
            print("Entrez une heure entre 0 et 23.")
        except ValueError:
            print("Veuillez entrer un entier.")

debut = saisir_heure("Heure de début (0-23) : ")
fin = saisir_heure("Heure de fin (0-23) : ")

heures_offpeak = 0
heures_peak = 0

heure = debut
while heure != fin:
    if heure < 7 or heure >= 17:
        heures_offpeak += 1
    else:
        heures_peak += 1
    heure = (heure + 1) % 24

duree = heures_offpeak + heures_peak
cout = heures_offpeak * 1 + heures_peak * 2

print("Durée (heures) :", duree)
print("Heures à 1€/h  :", heures_offpeak)
print("Heures à 2€/h  :", heures_peak)
print("Total à payer  :", cout, "€")