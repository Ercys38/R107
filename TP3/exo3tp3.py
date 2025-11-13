import random

x = random.randint(0, 100)
tours = 0

while True:
    try:
        guess = int(input("Devinez le nombre (entre 0 et 100) : "))
    except ValueError:
        print("Veuillez entrer un entier.")
        continue
    if guess < 0 or guess > 100:
        print("La valeur doit être comprise entre 0 et 100.")
        continue

    tours += 1

    if guess < x:
        print("Plus grand.")
    elif guess > x:
        print("Plus petit.")
    else:
        print(f"Bravo ! Le nombre était {x}. Trouvé en {tours} tour(s).")
        break