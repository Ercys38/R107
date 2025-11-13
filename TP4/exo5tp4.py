def est_bissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

s = input("Entrez une date au format jjmmaaaa : ").strip()

if len(s) != 8 or not s.isdigit():
    print("Format invalide : la date doit contenir exactement 8 chiffres (jjmmaaaa). Merci de corriger votre saisie.")
else:
    jj = int(s[0:2])
    mm = int(s[2:4])
    aaaa = int(s[4:8])

    if aaaa < 1:
        print("Date invalide : l’année doit être un entier positif (≥ 1).")
    elif mm < 1 or mm > 12:
        print("Date invalide : le mois doit être compris entre 1 et 12.")
    else:
        # Nombre de jours par mois
        jours_par_mois = [31, 29 if est_bissextile(aaaa) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        max_jours = jours_par_mois[mm - 1]

        if jj < 1:
            print("Date invalide : le jour doit être au moins 1.")
        elif jj > max_jours:
            # Messages détaillés selon le cas
            if mm == 2 and jj == 29 and not est_bissextile(aaaa):
                print(f"Date invalide : le 29 février n’existe pas en {aaaa} (année non bissextile).")
            elif jj == 31 and mm in (4, 6, 9, 11):
                print(f"Date invalide : le mois {mm} compte 30 jours, donc le 31 n’existe pas.")
            else:
                print(f"Date invalide : le mois {mm} compte {max_jours} jours.")
        else:
            print(f"Date valide : {jj:02d}/{mm:02d}/{aaaa}")