def ajouter_elt(lst, elt):
    lst.append(elt)
    return lst

print("Fonction ajouter_elt définie avec succès !")

lst1 = [0, 1, 2]
print("lst1 :", lst1)
print("Type :", type(lst1))
print("ID :", id(lst1))

lst2 = ajouter_elt(lst1, len(lst1))
print("lst2 :", lst2)
print("Type :", type(lst2))
print("ID :", id(lst2))

print("lst1 - Contenu:", lst1, "Type:", type(lst1), "ID:", id(lst1))
print("lst2 - Contenu:", lst2, "Type:", type(lst2), "ID:", id(lst2))

print("Les deux listes ont le MÊME identifiant !")
print("lst1 et lst2 pointent vers le MÊME objet en mémoire.")
print()
print("Explication :")
print("- La fonction ajouter_elt modifie la liste lst directement (lst.append)")
print("- Puis elle retourne cette même liste modifiée")
print("- lst2 n'est pas une nouvelle liste, c'est une référence à lst1")
print("- Les deux variables pointent vers le même objet mémoire")
print()
print("Ceci illustre le concept d'EFFET DE BORD mentionné dans le cours :")
print("Python transmet les arguments par référence, donc quand on")
print("modifie une liste dans une fonction, l'objet original est modifié.")
print()
print("Vérification : lst1 est lst2 ? ", lst1 is lst2)