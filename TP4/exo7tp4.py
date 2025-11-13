login1 = "Ercys38"
login2 = input("Entrez le login de votre binôme : ")
binome = (login1, login2)
print(f"L’étudiant {binome[0]} est en binome avec l’étudiant {binome[1]}")


nouveau_login2 = input("Entrez le nouveau login pour votre binôme : ")
try:
    binome[1] = nouveau_login2
except TypeError as e:
    print("Observation (modification) : impossible de modifier un élément d’un tuplet (immutable).")
    print(f"Exception : {e}")
print(f"Le tuplet actuel reste inchangé : {binome}")


try:
    del binome[1]
except TypeError as e:
    print("Observation (suppression) : impossible de supprimer un élément d’un tuplet (immutable).")
    print(f"Exception : {e}")
print(f"Le tuplet actuel reste inchangé : {binome}")

#
login3 = input("Entrez le login du troisième membre pour former un trinôme : ")
trinome = binome + (login3,)
print(f"Trinôme formé : {trinome}")
print("Conclusion : les tuplets (tuples) sont immuables. Pour modifier, supprimer ou ajouter,")
print("il faut créer un nouveau tuplet (par concaténation) ou passer par une liste puis reconvertir.")