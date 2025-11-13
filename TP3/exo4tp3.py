n = int(input("Entrez n (>= 0) : "))
choix = input("Choisissez la boucle (for/while) : ").strip().lower()

fact = 1
if choix.startswith("f"):
    for i in range(1, n + 1):
        fact *= i
        print(f"{i}! = {fact}")
else:
    i = 1
    while i <= n:
        fact *= i
        print(f"{i}! = {fact}")
        i += 1

print(f"Résultat: {n}! = {fact}")