nMax = 10
v1 = []
v2 = []

while True:
    try:
        n = int(input(f"Quelle est la taille de vos vecteurs [entre 1 et {nMax}] ? "))
        if 1 <= n <= nMax:
            break
    except ValueError:
        pass

print("Saisie du premier vecteur :")
for i in range(n):
    while True:
        try:
            val = int(input(f"v1[{i}] = "))
            v1.append(val)
            break
        except ValueError:
            pass

print("Saisie du second vecteur :")
for i in range(n):
    while True:
        try:
            val = int(input(f"v2[{i}] = "))
            v2.append(val)
            break
        except ValueError:
            pass

produit = sum(v1[i] * v2[i] for i in range(n))
print(f"Le produit scalaire de v1 par v2 vaut {float(produit):.1f}")