nombre = int(input("Entrez un nombre entier: "))


if nombre > 0:
    signe = "positif"
elif nombre < 0:
    signe = "négatif"
else:
    signe = "zéro"


if nombre % 2 == 0:
    parite = "pair"
else:
    parite = "impair"

if nombre == 0:
    print("Le nombre est zéro (et il est pair)")
else:
    print(f"Le nombre est {signe} et {parite}")
