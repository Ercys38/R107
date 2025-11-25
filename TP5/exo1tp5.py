
nom1 = input("Nom de la premiere personne : ")
prenom1 = input("Prenom de la premiere personne : ")


nom2 = input("Nom de la deuxieme personne : ")
prenom2 = input("Prenom de la deuxieme personne : ")


nom1_formate = nom1.upper()
prenom1_formate = prenom1.capitalize()

nom2_formate = nom2.upper()
prenom2_formate = prenom2.capitalize()


personne1 = f"{prenom1_formate} {nom1_formate}"
personne2 = f"{prenom2_formate} {nom2_formate}"


if (nom1_formate, prenom1_formate) <= (nom2_formate, prenom2_formate):
    print(personne1)
    print(personne2)
else:
    print(personne2)
    print(personne1)