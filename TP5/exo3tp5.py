chaine = input("Entrez un mot ou une phrase : ")

chaine_epuree = ""

for c in chaine:

    if c.isalpha():
        chaine_epuree += c.lower()

inverse = chaine_epuree[::-1]

if chaine_epuree == inverse and chaine_epuree != "":
    print("C'est un palindrome !")
else:
    print("Ce n'est pas un palindrome.")