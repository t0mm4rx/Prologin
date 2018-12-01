#coding: utf-8

import random

n = 2000
m = 10

tailles = [0] * n
motif = [0] * m

for i in range(len(tailles)):
    tailles[i] = str(random.randint(1, 15))

for i in range(len(motif)):
    motif[i] = str(i + 1)

print(str(m) + " " + str(n))

print(" ".join(motif))
print(" ".join(tailles))
