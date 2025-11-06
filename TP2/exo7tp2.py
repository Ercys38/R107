import random

tirage = random.randint(0, 100)
if tirage < 66:
    print("Pile !")
else:
    print("Face !")
