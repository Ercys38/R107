s = input("Vous cherchez la table de multiplication de quel nombre ?\n")
try:
    x = float(s)
except ValueError:
    print("Entrée invalide. Veuillez saisir un nombre réel.")
    exit(1)

resultats = [round(x * i, 1) for i in range(10)]

for i, res in enumerate(resultats):
    print(f"{round(x, 1)} * {i} = {res}")