import random

tipps = input("Geben sie die Anzahl von Tipps ein: ")
tipps = int(tipps)

min = 1
max = 45

while tipps > 0:
    anzahl_zahlen_pro_tipp = 0
    tipp = []
    while anzahl_zahlen_pro_tipp < 6:
        random_number = random.randint(min, max)
        if random_number not in tipp:
            tipp.append(random_number)
            anzahl_zahlen_pro_tipp = anzahl_zahlen_pro_tipp + 1
    tipps = tipps - 1
    tipp.sort()
    print(tipp)
