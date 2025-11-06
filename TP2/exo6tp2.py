import random

tirage = random.randint(0, 100)

if tirage < 50:
    print("Pile !")
else:
    print("Face !")
