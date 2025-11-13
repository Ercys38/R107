import time

n = -1
while n < 0:
    try:
        n = int(input("Entrez un entier positif n : "))
    except ValueError:
        n = -1

i = n
while i >= 0:
    print(i)
    time.sleep(1)
    i -= 1