N = -1
while N < 0:
    N = int(input("Entrez N (entier >= 0) : "))
somme = 0
for i in range(N + 1):
    somme += i
print("Somme des entiers de 0 à", N, "=", somme)

valeur = None
while valeur != 100:
    valeur = int(input("Entrez 100 pour arrêter : "))
print("Fin de l'attente.")

moins_10 = 0
entre_10_15 = 0
plus_ou_egal_15 = 0
for i in range(10):
    x = -1.0
    while x < 0 or x > 20:
        x = float(input("Valeur " + str(i + 1) + "/10 (entre 0 et 20) : "))
    if x < 10:
        moins_10 += 1
    elif x < 15:
        entre_10_15 += 1
    else:
        plus_ou_egal_15 += 1
print("Nombre de valeurs < 10           :", moins_10)
print("Nombre de valeurs dans [10, 15[  :", entre_10_15)
print("Nombre de valeurs >= 15          :", plus_ou_egal_15)

X = 1
while X <= 1:
    X = int(input("Entrez X (> 1) : "))
n = 0
somme = 0
while somme + (n + 1) <= X:
    n += 1
    somme += n
print("N =", n)