L1 = [2, 7, 5, 6, 7, 1, 6, 2, 1, 7, 6]

max_count = -1
most = None

for x in L1:
    c = L1.count(x)
    if c > max_count:
        max_count = c
        most = x

print(f"Le nombre le plus frequent dans la liste est le : {most} ({max_count} x)")