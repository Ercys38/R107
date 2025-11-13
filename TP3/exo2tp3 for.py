import time

n = -1
while n < 0:
    try:
        n = int(input("Entrez un entier positif n : "))
    except ValueError:
        n = -1

for i in range(n, -1, -1):
    print(i)
    time.sleep(1)