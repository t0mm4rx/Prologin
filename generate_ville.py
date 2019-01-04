import sys
import random
import math

n = int(sys.argv[1])
l = random.randint(int(math.floor(n / 2)), int(n * 2))
g = random.randint(int(math.floor(n / 10)), math.floor(int(n / 2)))

retards = []
lignes = []
gares = []

for i in range(n):
    retards.append(random.randint(1, 10))

for i in range(l):
    lignes.append([random.randint(1, n + 1), random.randint(1, n + 1), random.randint(1, 15)])

for i in range(g):
    gares.append([random.randint(1, n + 1), random.randint(1, n + 1), random.randint(1, 10)])


with open('villesg', 'w+') as file:
    file.write(str(n) + " ")
    file.write(str(l) + " ")
    file.write(str(g) + "\n")
    for r in retards:
        file.write(str(r) + "\n")

    for line in lignes:
        file.write(str(line[0]) + " " + str(line[1]) + " " + str(line[2]) + "\n")

    for gare in gares:
        file.write(str(gare[0]) + " " + str(gare[1]) + " " + str(gare[2]) + "\n")
