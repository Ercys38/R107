def taille_chaine(chaine):
    """Retourne la taille de la chaîne en comptant caractère par caractère."""
    compteur = 0
    for _ in chaine:
        compteur += 1
    return compteur




def pourcentage_voyelles(chaine):
    """Retourne le pourcentage de voyelles (a, e, i, o, u, y) dans la chaîne."""
    voyelles = "aeiouyAEIOUY"
    nb_voyelles = 0
    taille = taille_chaine(chaine)

    if taille == 0:
        return 0.0

    for c in chaine:

        for v in voyelles:
            if c == v:
                nb_voyelles += 1
                break

    return nb_voyelles * 100.0 / taille




def indice_premiere_occurrence(chaine, motif):
    """
    Retourne l'indice de début de la première occurrence de 'motif' dans 'chaine'
    ou -1 si le motif n'est pas trouvé.
    (Équivalent simplifié de find, mais fait à la main.)
    """
    n = taille_chaine(chaine)
    m = taille_chaine(motif)

    if m == 0 or m > n:
        return -1


    for i in range(n - m + 1):

        j = 0
        while j < m and chaine[i + j] == motif[j]:
            j += 1
        if j == m:
            return i
    return -1

def nombre_occurrences(chaine, motif):
    """
    Compte le nombre d'occurrences (possiblement chevauchées) de 'motif' dans 'chaine'.
    """
    n = taille_chaine(chaine)
    m = taille_chaine(motif)

    if m == 0 or m > n:
        return 0

    compteur = 0

    for i in range(n - m + 1):
        j = 0
        while j < m and chaine[i + j] == motif[j]:
            j += 1
        if j == m:
            compteur += 1

    return compteur



def main():
    T = input("Entrez une chaîne de caractères (max 100 caractères) : ")


    taille = taille_chaine(T)
    print(f"Taille de la chaîne : {taille}")


    pct_voyelles = pourcentage_voyelles(T)
    print(f"Pourcentage de voyelles : {pct_voyelles:.2f}%")


    motif = "wagon"
    indice = indice_premiere_occurrence(T, motif)
    if indice != -1:
        print(f'La chaîne "{motif}" est une sous-chaîne, première occurrence à l’indice {indice}.')
    else:
        print(f'La chaîne "{motif}" n’est pas une sous-chaîne.')


    nb_occ = nombre_occurrences(T, motif)
    print(f'Nombre d’occurrences de "{motif}" : {nb_occ}')


if __name__ == "__main__":
    main()