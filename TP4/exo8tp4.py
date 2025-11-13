dic1 = {
    "firstname": input("Prénom : "),
    "name": input("Nom : "),
    "promo": int(input("Promo (année) : ")),
    "group": int(input("Groupe de TP : "))
}

print(f"votre nom est ‘{dic1['name']}’, prénom est ‘{dic1['firstname']}’, vous faites partie de la promo ‘{dic1['promo']}’ et votre groupe est ‘{dic1['group']}’")

print("Les clés du dictionnaire sont :")
for k in dic1:
    print(f"-{k}")

print("Les valeurs du dictionnaire sont :")
for v in dic1.values():
    print(f"-{v}")

print("Les tuplets du dictionnaire sont :")
for k, v in dic1.items():
    print(f"-('{k}', {v})")

print("\nSaisie du binôme :")
dic2 = {
    "firstname": input("Prénom : "),
    "name": input("Nom : "),
    "promo": int(input("Promo (année) : ")),
    "group": int(input("Groupe de TP : "))
}

binome = {
    input("Identifiant pour vous : "): dic1,
    input("Identifiant pour votre binôme : "): dic2
}

print("Les étudiants formants le binôme sont :")
for etu in binome.values():
    print(f"- L'étudiant {etu['name']} {etu['firstname']} du groupe {etu['group']}")