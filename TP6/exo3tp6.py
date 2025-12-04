def ajouter_elt(lst=[0,1,2], elt=3):
    lst.append(elt)
    return lst

resultat1 = ajouter_elt()
print("Résultat :", resultat1)
print("ID de la liste retournée :", id(resultat1))


print("\nAppel 2 :")
resultat2 = ajouter_elt()
print("Résultat :", resultat2)
print("ID de la liste retournée :", id(resultat2))

print("\nAppel 3 :")
resultat3 = ajouter_elt()
print("Résultat :", resultat3)
print("ID de la liste retournée :", id(resultat3))

print("\nAppel 4 :")
resultat4 = ajouter_elt()
print("Résultat :", resultat4)
print("ID de la liste retournée :", id(resultat4))

print("À chaque appel, la liste continue de s'agrandir !")
print("Tous les appels ont le MÊME ID !")
print()
print("Explication :")
print("- La valeur par défaut [0,1,2] est créée UNE SEULE FOIS")
print("  lors de la DÉFINITION de la fonction (pas à chaque appel)")
print("- Cette liste par défaut est stockée en mémoire et réutilisée")
print("- À chaque appel sans argument, on modifie LA MÊME liste")
print("- C'est un PIÈGE classique en Python !")
print()
print("Solution : Ne JAMAIS utiliser un objet mutable (liste, dict)")
print("comme valeur par défaut.  Utiliser None à la place.")


def ajouter_carac(ch="abc", elt="d"):
    return ch + elt

print("Fonction ajouter_carac définie avec succès !")

resultat_ch1 = ajouter_carac()
print("Résultat :", resultat_ch1)
print("ID du résultat :", id(resultat_ch1))


print("\nAppel 2 :")
resultat_ch2 = ajouter_carac()
print("Résultat :", resultat_ch2)
print("ID du résultat :", id(resultat_ch2))

print("\nAppel 3 :")
resultat_ch3 = ajouter_carac()
print("Résultat :", resultat_ch3)
print("ID du résultat :", id(resultat_ch3))

print("\nAppel 4 :")
resultat_ch4 = ajouter_carac()
print("Résultat :", resultat_ch4)
print("ID du résultat :", id(resultat_ch4))

print("Le résultat est TOUJOURS 'abcd' !")
print("Les ID peuvent être identiques ou différents (optimisation Python)")
print()
print("Explication de la différence avec ajouter_elt :")
print("- Les chaînes de caractères sont IMMUTABLES")
print("- L'opération ch + elt crée une NOUVELLE chaîne à chaque fois")
print("- On ne modifie pas la valeur par défaut, on en crée une nouvelle")
print("- Les paramètres par défaut 'abc' et 'd' restent inchangés")
print()
print("Comparaison :")
print("- Liste (mutable) : la valeur par défaut est MODIFIÉE à chaque appel")
print("- String (immutable) : la valeur par défaut reste INTACTE")
print("- C'est pourquoi on obtient toujours 'abcd' avec ajouter_carac")
print("  mais une liste qui s'agrandit avec ajouter_elt")

print("✗ DANGER : Objets mutables (liste, dict, set) comme défaut")
print("✓ SÉCURISÉ : Objets immutables (int, float, str, tuple, None) comme défaut")
print()
print("Bonne pratique pour les listes :")
print("def ajouter_elt_safe(lst=None, elt=3):")
print("    if lst is None:")
print("        lst = [0, 1, 2]")
print("    lst.append(elt)")
print("    return lst")